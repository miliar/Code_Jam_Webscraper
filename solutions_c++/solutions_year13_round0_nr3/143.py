#include <iomanip>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

typedef long long ll;
typedef vector<int> VE;
const ll base = 1000000000; // 9 zeros

class BI { public:
VE v;    // el digit menys significatiu es v[0]
int n;   // v.size()
mutable int sig; // 1: positiu o zero, -1: negatiu

// GENERAL PER A TOT
void zero() { v = VE(1, 0); n = sig = 1; }
void remida(int i, int que=0) { v.resize(n = i, que); }

void treuzeros(){
  while (--n and !v[n]);
  remida(n+1);
  if (n == 1 and !v[0]) sig = 1;
}

void parse(string num) {
  if (num[0] == '-') { sig = -1; num = num.substr(1); }
    else sig = 1;
  int m = num.size() - 1;
  v = VE(1 + m/9, 0); n = v.size();
  for (int i = m, exp = 0, pw = 1, pos = 0; i >= 0; --i, ++exp, pw *= 10) {
    if (exp == 9) { exp = 0; pw = 1; ++pos; }
    v[pos] += (num[i] - '0')*pw;
  }
  treuzeros();
}

// DESIGUALTATS
// compara en valor absolut, 0: == b, positiu: > b; negatiu: < b
inline int compabs(const BI &b) const {
  if (n != b.n) return n - b.n;
  for (int i = n - 1; i >= 0; --i)
    if (v[i] != b.v[i]) return v[i] - b.v[i];
  return 0;
}

// 0: == b, positiu: > b; negatiu: < b
inline int compara(const BI &b) const {
  if (sig != b.sig) return sig - b.sig;
  return sig*compabs(b);
}

inline bool operator==(const BI &b) const { return !compara(b); }
inline bool operator!=(const BI &b) const { return compara(b); }
inline bool operator<(const BI &b)  const { return compara(b) < 0; }
inline bool operator<=(const BI &b) const { return compara(b) <= 0; }
inline bool operator>(const BI &b)  const { return compara(b) > 0; }
inline bool operator>=(const BI &b) const { return compara(b) >= 0; }

// $|x| < 10^9$
inline bool operator==(int x) const { return n == 1 and sig*v[0] == x; }

// OPERACIONS EN VALOR ABSOLUT
inline int dig(int i) const { return (i < n ? v[i] : 0); }

void suma(const BI &b) {
  if (n < b.n) remida(b.n, 0);
  int ca = 0;
  for (int i = 0; i < n; ++i) {
    v[i] += b.dig(i) + ca; ca = v[i]/base; v[i] %= base;
  }
  if (ca) remida(n+1, ca);
}

// suposa >= b
void resta(const BI &b) {
  int ca = 0;
  for (int i = 0; i < n; ++i) {
    v[i] += base - b.dig(i) + ca; ca = v[i]/base - 1; v[i] %= base;
  }
  treuzeros();
}

// INICIALITZACIONS I COPIA
BI() { zero(); }
BI(const BI &b) { *this = b; }

// $|x| < 10^{18}$
BI(ll x) {
  sig = (x < 0 ? -1 : 1); x *= sig;
  if (x < base) { v = VE(1, x); n = 1; }
    else { v = VE(2); v[0] = x % base; v[1] = x/base; n = 2; }
}

BI(string num) { parse(num); }
void operator=(const BI &b) { v = b.v; n = b.n; sig = b.sig; }

// OPERACIONS
void operator+=(const BI &b) {
  if (sig == b.sig) return suma(b);
  if (compabs(b) >= 0) return resta(b);
  BI aux(b); aux.resta(*this); *this = aux;
}

void operator-=(const BI &b) {
  if (&b == this) return zero();
  b.sig *= -1; operator+=(b); b.sig *= -1;
}

// $|x| < 10^9$
void operator*=(int x) {
  if (x < 0) { sig *= -1; x *= -1; }
  remida(n + 1, 0);
  ll ca = 0;
  for (int i = 0; i < n; ++i) {
    ca += (ll)v[i]*x; v[i] = ca % base; ca /= base;
  }
  treuzeros();
}

void operator*=(BI &b) {
  BI c; c.remida(n + b.n, 0); c.sig = sig*b.sig;
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < b.n; ++j) {
      int k = i + j;
      ll z = (ll)v[i]*b.v[j] + c.v[k], y;
      while ((y = z / base)) { c.v[k] = z % base; z = y + c.v[++k]; }
      c.v[k] = z;
    }
    c.treuzeros();
    *this = c;
}

// $|x| < 10^9$
void operator/=(int x) {
  if (x < 0) { sig *= -1; x *= -1; }
  ll ca = 0;
  for (int i = n-1; i >= 0; --i ) {
    ca += v[i]; v[i] = ca/x; ca %= x; ca *= base;
  }
  treuzeros();
}

void operator/=(const BI &b){
  if (compabs(b)<0) return zero();
  if (b.n==1) *this/=b.sig*b.v[0];
  else {
    int st = sig*b.sig, sb = b.sig; sig = b.sig = 1;
    vector<BI> VB,pot2;
    VB.push_back(b); pot2.push_back(1);
    BI curr=0;
    //primera pasada
    while (VB[VB.size()-1]<=*this){
      BI ultimo=VB[VB.size()-1];  ultimo+=ultimo; VB.push_back(ultimo);
      ultimo=pot2[pot2.size()-1]; ultimo+=ultimo; pot2.push_back(ultimo);
    }
    curr+=pot2[pot2.size()-2]; (*this)-=VB[VB.size()-2];
    //resto
    while ((*this)>=b){
      int i=0;
      while (VB[i]<=(*this)) i++;
      curr+=pot2[i-1]; (*this)-=VB[i-1];
    }
    (*this)=curr; sig = st; b.sig = sb;
  }
}

// $|x| < 10^9$; amb negatius funciona com C++
ll mod(int x) const {
  if (x < 0) x *= -1;
  ll ca = 0;
  for (int i = n-1; i >= 0; --i ) { ca *= base; ca += v[i]; ca %= x; }
  return ca;
}

void operator%=(BI &b) {
  BI r(*this); r /= b; r*= b; operator-=(r);
}

};

ostream& operator<<(ostream& out, const BI &b) {
  if (b.sig < 0) out << '-';
  int i = b.v.size() - 1;
  out << b.v[i];
  for (--i; i >= 0; --i) out << setw(9) << setfill('0') << b.v[i];
  return out;
}

istream& operator >>(istream& in, BI &b) {
  string num; in >> num; b.parse(num);
  return in;
}

bool palindrome(BI n) {
  stringstream ss;
  ss << n;
  string s = ss.str();
  int m = s.size();
  for (int i = 0; i < m; ++i)
    if (s[i] != s[m - 1 - i]) return false;
  return true;
}

bool check(BI n) {
  if (not palindrome(n)) return false;
  BI s = n;
  s *= n;
  return palindrome(s);
}

int find_first(BI a, const vector<BI>& v) {
  int e = 0, d = v.size() - 1;
  while (e <= d) {
    int m = (e + d)/2;
    if (a <= v[m]) d = m - 1;
    else e = m + 1;
  }
  return d + 1;
}

int find_last(BI b, const vector<BI>& v) {
  int e = 0, d = v.size() - 1;
  while (e <= d) {
    int m = (e + d)/2;
    if (v[m] <= b) e = m + 1;
    else d = m - 1;
  }
  return e - 1;
}

int main() {
  vector<set<string> > V(60);
  V[1].insert("1");
  V[1].insert("2");
  V[1].insert("3");
  for (int i = 2; i < 60; ++i) {
    string sp1 = "1" + string(i - 2, '0') + "1";
    string sp2 = "2" + string(i - 2, '0') + "2";
    BI tp1(sp1);
    BI tp2(sp2);
    if (check(tp1)) V[i].insert(sp1);
    if (check(tp2)) V[i].insert(sp2);
    for (int j = 0; j < i/2; ++j) {
      set<string>& st = V[i - 2 - 2*j];
      for (set<string>::iterator it = st.begin(); it != st.end(); ++it) {
        string s = *it;
        string s1 = "1" + string(j, '0') + s + string(j, '0') + "1";
        string s2 = "2" + string(j, '0') + s + string(j, '0') + "2";
        BI t1(s1);
        BI t2(s2);
        if (check(t1)) V[i].insert(s1);
        if (check(t2)) V[i].insert(s2);
      }
    }
  }
  
  vector<BI> pals;
  for (int i = 0; i < 60; ++i) {
    for (set<string>::iterator it = V[i].begin(); it != V[i].end(); ++it) {
      BI num(*it);
      num *= num;
      pals.push_back(num);
    }
  }
  
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    BI a, b;
    cin >> a >> b;
    cout << "Case #" << cas << ": " << find_last(b, pals) - find_first(a, pals) + 1 << endl;
  }
}
