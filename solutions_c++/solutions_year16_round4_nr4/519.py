#include <bits/stdc++.h>
using namespace std;

#define SZ(x) ((int)(x).size())
#define ALL(x) x.begin(), x.end()
#define REP(i,n) for(int i = 0; i < int(n); ++i)
#define REPE(i, a, b) for(int i = (a); i <= int(b); ++i)
#define DB(x) cerr << __LINE__ << ": " << #x << " = " << (x) << endl
#define MP make_pair
#define PB push_back
#define EB emplace_back
#define BR putchar('\n')
#define MS0(ar) memset(ar, 0, sizeof(ar))
#define MS1(ar) memset(ar, -1, sizeof(ar))
#define F first
#define S second
#define MP make_pair
#define MT make_tuple

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair<int, int> PII;
typedef complex<double> CD;

void R(int &x) { scanf("%d", &x); }
void R(LL &x) { scanf("%lld", &x); }
void R(ULL &x) { scanf("%llu", &x); }
void R(double &x) { scanf("%lf", &x); }
void R(LD &x) { scanf("%Lf", &x); }
template<typename T> void R(T &t) { cin >> t; }
template<typename T> void R(vector<T> &ar) { for(auto &it : ar) R(it); }
template<typename T, typename... Args> void R(T &t, Args&... args) {
  R(t);
  R(args...);
}

void W(const char &c) { putchar(c); };
void W(const int &x) { printf("%d", x); }
void W(const LL &x) { printf("%lld", x); }
void W(const ULL &x) { printf("%llu", x); }
void W(const double &x) { printf("%lf", x); }
void W(const LD &x) { printf("%Lf", x); }
template<typename T> void W(const T &t) { cout << t; }
template<typename T> void W(const vector<T> &ar) {
  for(size_t i = 0; i < ar.size(); ++i) {
    W(ar[i]);
    putchar(" \n"[i + 1u == ar.size()]);
  }
}
template<typename T, typename... Args> void W(const T &t, const Args&... args) {
  W(t);
  W(args...);
}

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};
const int maxn = 100010;
const double eps = 1e-8;

int n;
char g[33][33];
int oc;
int p[22];
int f(int xx) {
  if(xx == n) return true;
  const int x = p[xx];
  bool fnd = false;
  for(int i = 0; i < n; ++i) if(g[x][i] == '1' and (oc & (1 << i)) == 0) {
    fnd = true;
    oc ^= 1 << i;
    if(!f(xx + 1)) return false;
    oc ^= 1 << i;
  }
  return fnd;
}

bool ok() {
  REP(i, n) p[i] = i;
  do {
    oc = 0;
    if(!f(0)) return false;
  } while(next_permutation(p, p + n));
  return true;
}

int main() {
  int T;
  R(T);
  for(int kase = 1; kase <= T; ++kase) {
    R(n);
    REP(i, n) scanf("%s", g[i]);
    const int m = 1 << (n * n);
    int ans = n * n;
    REP(b, m) {
      bool gg = false;
      const int cnt = __builtin_popcount(b);
      if(cnt >= ans) continue;
      REP(i, n) REP(j, n) {
        const int t = i * n + j;
        if((b & (1 << t)) and g[i][j] == '1') {
          gg = true;
          break;
        }
      }
      if(gg) continue;
      REP(i, n) REP(j, n) {
        const int t = i * n + j;
        if((b & (1 << t))) {
          g[i][j] = '1';
        }
      }
      if(ok()) {
        ans = min(ans, cnt);
      }
      REP(i, n) REP(j, n) {
        const int t = i * n + j;
        if((b & (1 << t))) {
          g[i][j] = '0';
        }
      }
    }
    printf("Case #%d: %d\n", kase, ans);
  }
  return 0;
}
