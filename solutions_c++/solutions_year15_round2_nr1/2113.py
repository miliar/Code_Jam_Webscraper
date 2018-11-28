#include <bits/stdc++.h>
#define CASES_DEFAULT_CORES 1
// global memo would fail w/ threads
#define MAXCASES 100
#include "codejam.hh"
#define MAXDIGITS 16
#define MAXSMALL 1000000

typedef unordered_map<u64, u64> Memo; // holds only lsd=1 keys. TODO: hash on Digs directly?
Memo memo;

/// lsb first; return ptr 1 past final digit (msb)
template <class u64>
char *digs(u64 x, char *d) {
  assert(x);
  for(;;) {
    *d++ = x % 10;
    x /= 10;
    if (!x) return d;
  }
}

template <class u64>
u64 rev(u64 n) {
  char d[MAXDIGITS];
  char *e = digs(n, d);
  u64 unit = 1, sum = 0;
  while (--e >= d) {
    sum += *e * unit;
    //CO4("rev", (int)*e, unit, sum);
    unit *= 10;
  }
  return sum;
}

template <class u64>
u64 sup10(u64 n) {
  u64 unit = 10;
  while (unit < n) {
    unit *= 10;
  }
  return unit;
}

u64 sol(u64 n) {
  if (n <= 20) return n;
  u64 lsd = n % 10;
  if (lsd) {
  u64 nr = rev(n);
  if (nr < n) {
    CO3("reversing", n, nr);
    return 1+sol(nr);
  }
  }
  u64 s10 = sup10(n);
  u64 msd = 10*n / s10;
  if (msd == 1) {
    U n1000 = s10/10;
    u64 n991 = n1000 - 9;
    CO3("1... stepping to ...991", n, n991);
    return (n - n991) + sol(n991);
  }
  u64 steps = lsd == 0 ? 9 : (lsd - 1);
  n -= steps;
  CO5("adjusted n", lsd, msd, steps, n);
  assert(n % 10 == 1);
  u64 &ans = memo[n];
  if (ans)
    return steps + ans;
  return ans ? ans : (ans = 1 + steps + sol(rev(n)));
}

U smemo[MAXSMALL + 1];

U smallsol(U n) {
  assert(n <= MAXSMALL);
  U &ans = smemo[n];
  if (n <= 20) return ans = n;
  if (ans) return ans;
  U lsd = n % 10;
  U best = (U)-1;
  assert(n);
  U prev = smemo[n - 1];
  ans = prev + 1;
  if (lsd) {
    U nr = rev(n);
    if (nr + 1 < n) {
      assert(nr);
      CO3("reversing", n, nr);
      assert(smemo[nr]);
      amin(ans, 1 + smemo[nr]);
    }
  }
  //CO3("ans", n, ans);
  return ans;
}

U solv(U n) {
  REP(i, n) {
    smallsol(i);
  }
  return smallsol(n);
}

struct Count : CaseBase {
  u64 N;
  u64 steps;
  void solve() {
    steps = solv(N);
  }
  void read() {
    N = GETu64;
  }
  void show1() {
    cerr << N << ' ';
  }
  void print() {
    PUTu64(steps);
  }

};

CASES_MAIN(Count)
