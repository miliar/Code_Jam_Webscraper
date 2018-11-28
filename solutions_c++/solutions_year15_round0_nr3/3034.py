#define MAXCASES 100
#define MAXL 10000
#define MAXX 1000000000000llu
#define MAXLOG2X 64
#define MAXLREPS 15
#include "codejam.hh"

/// p: plus, m: minus
enum Q : u8 { p1, pi, pj, pk, m1, mi, mj, mk };
/// no-shift for p, shift for m
char qch[] = "1ijk!IJK";
Q qtimestable_pos[4][4] = {{p1, pi, pj, pk}, {pi, m1, pk, mj}, {pj, mk, m1, pi}, {pk, pj, mi, m1}};
Q qtimestable[8][8];

Q ijk(char c) {
  switch (c) {
    case 'i':
      return pi;
    case 'j':
      return pj;
    case 'k':
      return pk;
    default:
      abort();
  }
}

std::ostream& operator<<(std::ostream& out, Q q) {
  return out << qch[q];
}

bool negative(Q q) {
  return q & 4;
}
Q negated(Q q) {
  return Q(q ^ 4);
}
Q abs(Q q) {
  return Q(q & 3);
}

void init_qtimestable() {
  for (U i = 0; i < 4; ++i)
    for (U j = 0; j < 4; ++j) {
      // CO4("times", Q(i), Q(j), qtimestable_pos[i][j]);
      qtimestable[i + 4][j] = qtimestable[i][j + 4]
          = negated(qtimestable[i][j] = qtimestable[i + 4][j + 4] = qtimestable_pos[i][j]);
    }
}

Q qtimes(Q a, Q b) {
  return qtimestable[a][b];
}

Q qtimes(char a, char b) {
  return qtimestable[a][b];
}

bool qreal(Q a) {
  return !(a&3);
}

Q qsqr(Q a) {
  return qreal(a) ? p1 : m1;
}

Q qpow(Q x, u64 n) {
  if (x == p1) return p1;
  if (x == m1) return n & 1 ? m1 : p1;
  assert(qtimes(x, x) == m1);
  /// therefore x^4 = 1
  switch (n & 3) {
    case 0:
      return p1;
    case 1:
      return x;
    case 2:
      return m1;
    case 3:
      return negated(x);
  }
  abort();
}

Q& qltimeseq(Q& a, Q b) {
  return a = qtimes(a, b);
}

Q& qrtimeseq(Q a, Q& b) {
  return b = qtimes(a, b);
}

Q const prod_ijk = m1;

struct Qs : CaseBase {
  Q x[MAXL * MAXLREPS];
  U L;
  u64 X;

  static void init() {
    init_qtimestable();
    assert(prod_ijk == qtimes(qtimes(pi, pj), pk));
    assert(prod_ijk == qtimes(pi, qtimes(pj, pk)));
  }
  void read() {
    L = GETU;
    assert(L);
    X = GETu64;
    assert(X);
    REP(i, L) x[i] = ijk(getC());
  }
  void show1() {
    cerr << X << ' ';
    REP(i, L) cerr << x[i];
    cerr << " (" << L << "*" << X << " => " << L* X << ")";
  }
  void print() {
    yesno(yes);
    verbose = 0;
  }
  bool yes;

  void expand(U repeats) {
    assert(sizeof(Q) == 1);
    size_t bytes = sizeof(Q) * L;
    char* o = (char*)x;
    REP(i, repeats) memcpy(o += bytes, x, bytes);
  }
  void expandto(U to) {
    assert(to > 0);
    expand(to - 1);
  }
  Q qprod(Q* i, Q* e) {
    Q r = p1;
    assert(i < e);
    for (; i != e; ++i) r = qtimes(r, *i);
    return r;
  }
  void solve() {
    yes = false;
    if (X < 3 && L <= 1) return;
    if (X <= 1 && L < 3) return;
    Q prod = qprod(x, x + L);
    CO2("L^1", prod);
    if (prod == p1) return;
    Q full = qpow(prod, X);
    CO3("L^X", X, full);
    if (full != prod_ijk) return;
/**
   ijk = -1

   ij = k; so (ij)k must decompose into kk

   jk = i; so i(jk) must decompose into ii

   if we find any positions a < b where [0...a)=[a...L)=k and [0...b)=[b...L)=i then we're good

   it seems we can easily divide the basis unit vectors 1ijk, too. it seems
   that left and right division are different because times is
   noncommutative.

   so, it follows (i hope) that once we verify that the product of the L^X
   string is -1 = ijk, we know that wherever we find an i prefix, the rest
   is equal to -1 / i = i and wherever we find a k suffix, we know the rest
   (prefix to the left) is = k. so if there's any i prefix left of any k
   suffix we have j between them.

   this means that if X>1 and we have any left and right matches then we're
   done. but is it possible that we have no <L length prefix or suffix for
   X>1 but we do have one once we wrap around? and if so, how far do we have
   to look? obviously no more than 8 times through thanks to FSA
   intersection

*/
    // find true period: easy since we know prod is -1, so -1^X is alternating -1 1. period is 2 (-1^2 = 1) so
    // we can remove any 2*N things we want. how many do we need to leave behind? not sure! let's leave 12 +
    // parity(X) for now
    U period = 4;
    CO2("L^period repeats:", period);
    if (!period) return;
    assert(period <= MAXLREPS);
    U nrem = X % period;
    U needreps = period*3 + nrem;
    if (needreps > X) needreps = X;
    CO2("from X and this particular L, got X'=needreps", needreps);
    expandto(needreps);
    U XL = needreps * L;
    assert(XL > 1);
    VU lmatches;
    prod_matches(lmatches, x, XL, pi);
    if (lmatches.empty()) return;
    VU rmatches;
    rprod_matches(rmatches, x, XL, pk);
    if (rmatches.empty()) return;
    VU::const_iterator ri, rb = rmatches.begin(), re = rmatches.end();
    for (U l : lmatches) {
      Q m = p1;
      assert(l < XL);
      ri = rb;
      U rnext = *rb;
      for (int i = l + 1; i < XL - 1; ++i) {
        m = qtimes(m, x[i]);
        bool ism = m == pj;
        CO4("l->i = m (=pj?)", l, i, m);
        int afteri = i + 1;
        if (rnext < afteri)
          for (;;) {
            if (ri == re) goto next;
            rnext = *++ri;
            if (rnext == afteri && m == pj) {
            yes:  // could have used bitarray instead for checks - simpler code
              cpre() << " YES: " << l << ' ' << afteri << '\n';
              yes = true;
              return;
            }
            if (rnext > i) break;
          }
        else if (rnext == afteri && m == pj)
          goto yes;
      }
    next:
      CO2("no luck for", l);
    }
  }

  Q rprod(Q* i, Q* e) {
    Q r = p1;
    assert(i > e);
    for (--i; i >= e; --i) r = qtimes(*i, r);
    return r;
  }

  void prod_matches(VU& matches, Q* x, U n, Q match = pi) {
    Q r = p1;
    --n;
    for (U i = 0; i < n; ++i) {
      Q r_ = r;
      r = qtimes(r, x[i]);
      if (r == match) matches.push_back(i);
    }
    CO3("prods", match, showr(matches));
  }
  void rprod_matches(VU& matches, Q* x, U n, Q match = pk) {
    Q r = p1;
    while (n--) {
      Q r_ = r;
      r = qtimes(x[n], r);
      if (r == match) matches.push_back(n);
    }
    CO3("rprods", match, showr(matches));
    reversec(matches);
  }
};

CASES_MAIN(Qs)
