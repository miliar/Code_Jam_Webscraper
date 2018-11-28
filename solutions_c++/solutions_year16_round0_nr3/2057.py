#include <bits/stdc++.h>
using namespace std;

class BI {
typedef long long ll; typedef vector<int> VI;
const static ll base = 1000000000; // 9 zeros
friend ostream &operator<<(ostream &, const BI &);
friend istream &operator>>(istream &, BI &);
VI v;       // el digit menys significatiu es v[0]
int n, sig; // 1: positiu o zero, -1: negatiu
public: // INICIALITZACIONS I COPIA
BI() : v(1, 0), n(1), sig(1) {}
BI(ll x) { // $|x| < 10^{18}$
  sig = (x < 0 ? -1 : 1); x *= sig;
  if (x < base) v = {int(x)};
  else v = {int(x % base), int(x / base)};
  n = v.size();
}
BI(string num) : v(0), sig(1) {
  int p = 0;
  if (num[0] == '-') { sig = -1; ++p; }
  for (int i = int(num.size()); i > p; i -= 9) {
    int ini = max(p, i - 9); num[i] = '\0'; char *spam;
    v.push_back(strtol(&num[ini], &spam, 10));
  } treuzeros();
}
BI &treuzeros() {
  while (v.size() > 1 and v.back() == 0) v.pop_back();
  n = v.size(); if (n == 1 and v[0] == 0) sig = 1;
  return *this;
}
void resize(int m, int w = 0) { v.resize(n = m, w); }
int operator[](int i) const { return (i < n ? v[i] : 0); }

// OPERACIONS EN VALOR ABSOLUT
BI &suma_abs(const BI &b) { // operator=+
  if (n < b.n) resize(b.n); int ca = 0;
  for (int i = 0; i < n; ++i) {
    v[i] += b[i] + ca; ca = v[i] / base; v[i] %= base; }
  if (ca) resize(n + 1, ca);
  return *this;
}

BI &operator*=(const BI &b) {
  BI c; c.resize(n + b.n); c.sig = sig * b.sig;
  for (int i = 0; i < n; ++i) for (int j = 0; j < b.n; ++j) {
      int k = i + j; ll z = ll(v[i]) * b[j] + c[k];
      while (ll y = z / base) { c.v[k] = z % base; z = y + c.v[++k]; }
      c.v[k] = z;
    } return *this = c.treuzeros(); }

// BI &operator*=(ll x) { return operator*=(BI(x)); } // $|x| < 10^9$
BI &operator*=(int x) {
  if (x < 0) { sig = -sig; x = -x; }
  resize(n + 1); ll ca = 0;
  for (int i = 0; i < n; ++i) {
    ca += ll(v[i]) * x; v[i] = ca % base; ca /= base;
  } return treuzeros(); }
// Copy until here if you just want to add and multiply positive integers.

BI &resta_abs(const BI &b) { // abs(*this) >= abs(b)
  int ca = 0;
  for (int i = 0; i < n; ++i) {
    v[i] += base - b[i] + ca; ca = v[i] / base - 1; v[i] %= base;
  }
  return treuzeros(); }

// DESIGUALTATS
// compara en valor absolut, 0: == b, positiu: > b; negatiu: < b
int compabs(const BI &b) const {
  if (n != b.n) return n - b.n;
  for (int i = n - 1; i >= 0; --i)
    if (v[i] != b[i]) return v[i] - b[i];
  return 0;
}
// 0: == b, positiu: > b; negatiu: < b
int compara(const BI &b) const {
  if (sig != b.sig) return sig - b.sig;
  return sig * compabs(b);
}
bool operator==(const BI &b) const { return !compara(b); }
bool operator!=(const BI &b) const { return compara(b); }
bool operator<(const BI &b) const { return compara(b) < 0; }
bool operator<=(const BI &b) const { return compara(b) <= 0; }
bool operator>(const BI &b) const { return compara(b) > 0; }
bool operator>=(const BI &b) const { return compara(b) >= 0; }
// $|x| < 10^9$
bool operator==(int x) const { return n == 1 and sig * v[0] == x; }

// OPERACIONS
BI &operator+=(const BI &b) {
  if (sig == b.sig) return suma_abs(b);
  if (compabs(b) >= 0) return resta_abs(b);
  return *this = BI(b).resta_abs(*this);
}
BI operator-() const {
  if (operator==(0)) return *this;
  BI r(*this); r.sig *= -1; return r;
}
BI &operator-=(const BI &b) {
  if (&b == this) return *this = BI();
  return operator+=(-b);
}

// $|x| < 10^9$
BI &operator/=(int x) {
  if (x < 0) { sig *= -1; x *= -1; } ll ca = 0;
  for (int i = n - 1; i >= 0; --i) {
    ca += v[i]; v[i] = ca / x; ca %= x; ca *= base; }
  return treuzeros(); }

BI &operator/=(const BI &b) {
  if (compabs(b) < 0) return *this = BI();
  if (b.n == 1) return *this /= b.sig * b.v[0];
  int st = sig * b.sig; sig = 1;
  vector<BI> VB, pot2;
  VB.push_back(b.sig == 1 ? b : -b);
  pot2.push_back(1); BI curr = 0;
  while (VB[VB.size() - 1] <= *this) { // primera pasada
    BI ultimo = VB[VB.size() - 1]; ultimo += ultimo; VB.push_back(ultimo);
    ultimo = pot2[pot2.size() - 1]; ultimo += ultimo; pot2.push_back(ultimo);
  }
  curr += pot2[pot2.size() - 2];
  (*this) -= VB[VB.size() - 2];
  while ((*this) >= b) { // resto
    int i = 0; while (VB[i] <= (*this)) i++;
    curr += pot2[i - 1]; (*this) -= VB[i - 1];
  }
  (*this) = curr; sig = st; return *this; }

// $|x| < 10^9$; amb negatius funciona com C++
ll mod(int x) const {
  if (x < 0) x *= -1;
  ll ca = 0;
  for (int i = n - 1; i >= 0; --i) {
    ca *= base; ca += v[i]; ca %= x; }
  return ca; }

BI &operator%=(const BI &b) {
  BI r(*this); r /= b; r *= b; return operator-=(r); }

static BI gcdrec(BI &b, BI &c) {
  if (c == 0) return b; return gcdrec(c, b %= c); }

static BI gcd(const BI &b, const BI &c) {
  BI bb(b), cc(c); return gcdrec(bb, cc); }

void powrec(BI &aux, ll p) {
  if (!p) return;
  powrec(aux, p / 2); aux *= aux; if (p % 2) aux *= (*this); }

BI& pow(ll p) { BI aux(1); powrec(aux, p); return *this = aux; }

int log(int x) {
  BI a(*this);
  int n1 = (a.v.size() - 1) * 9 + (int)log10((double)a.v[v.size() - 1]);
  // n1 es nuestra aproximacion en base 10, es decir $10^{n1} <= N < 10^{n1+1}$
  // la aproximacion es exacta, ahora busquemos una aproximacion "aproximada"
  int abajo;
  abajo = (int)((double)(n1) / (log10((double)x)));
  BI b = x;
  b.pow((ll)abajo);
  BI c = b;
  c *= x;
  while (1) {
    if (c > a) return abajo;
    b = c; c *= x; abajo++;
  } }

BI& raizcu() { // raiz cuadrada
  if (*this == 0) return *this;
  vector<BI> divi;
  BI tab[10] = {(0), (1), (4), (9), (16), (25), (36), (49), (64), (81)};
  BI nueve(9), uno(1);
  divi.push_back(*this);
  while (*this >= 100) { *this /= 100; divi.push_back(*this); }
  BI res(0), cuad;
  for (int i = 1; i < 10; i++) {
    if (tab[i] > divi[divi.size() - 1].v[0]) {
      res = i - 1; cuad = tab[i - 1]; break;
    }
  }
  if (res == 0) { res = nueve; cuad = 81; }
  for (int i = divi.size() - 2; i >= 0; i--) {
    BI cienequiscu, veintecequis, c(0); bool b = false;
    cienequiscu = cuad; cienequiscu *= 100; veintecequis = res;
    veintecequis *= 20; cuad *= 100;
    for (int j = 1; j < 10; j++) {
      cienequiscu += veintecequis; cienequiscu += tab[j];
      if (cienequiscu > divi[i]) { b = true; res *= 10; res += c; break; }
      cuad = cienequiscu; cienequiscu -= tab[j]; c += uno;
    }
    if (!b) { res *= 10; res += nueve; }
  } return *this = res; }

BI& arrel(int x) { // raiz n-esima: lenta
  if (*this == 0) return *this;
  BI dre(1), q(1);
  do { dre += dre; for (int r = 0; r < x; ++r) q += q; } while (q <= *this);
  BI aux, esq(dre); esq /= 2;
  while (aux = dre, aux -= esq, aux != 1) {
    BI m(esq); m += dre; m /= 2; q = m; q.pow(x);
    if (q > *this) dre = m; else esq = m;
  } return *this = esq; }
};
ostream &operator<<(ostream &out, const BI &b) {
  if (b.sig < 0) out << '-'; out << b.v.back();
  for (int i = b.n - 2; i >= 0; --i)
    out << setw(9) << setfill('0') << b.v[i];
  return out;
}
istream &operator>>(istream &in, BI &b) {
  string num; in >> num; b = BI(num); return in;
}

using uint = BI;
using VI = vector<uint>;

uint primes[] = {2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37};

void bt(int i, int n, int &j, VI base, string &s) {
  if (j == 0) return;
  if (i == n) {
    VI div(11);
    for (int i = 2; i <= 10; ++i) {
      for (uint p : primes) {
        uint mod = base[i];
        mod %= p;
        if (mod == 0) {
          div[i] = p;
          break;
        }
      }
      if (div[i] == 0) return;
    }
    cout << s;
    for (int i = 2; i <= 10; ++i) cout << " " << div[i];
    cout << endl;
    --j;
    return;
  }
  for (int j = 2; j <= 10; ++j) base[j] *= j;
  
  s[i] = '0';
  if (i != 0 and i != n - 1) bt(i + 1, n, j, base, s);
  
  s[i] = '1';
  for (int j = 2; j <= 10; ++j) base[j] += 1;
  bt(i + 1, n, j, base, s);
}
int main() {
  int t;
  cin >> t;
  for (int z = 1; z <= t; ++z) {
    cout << "Case #" << z << ":" << endl;
    VI base(11);
    int n, j;
    cin >> n >> j;
    string s(n, '0');
    bt(0, n, j, base, s);
  }
}