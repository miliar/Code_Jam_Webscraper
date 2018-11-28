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

string dp[3][22] = {};
string f(int a, int b) {
  if(dp[a][b].size()) return dp[a][b];
  if(b == 0) {
    return dp[a][b] = "PRS"[a];
  }
  string s1, s2;
  s1 = f(a, b - 1);
  s2 = f(a == 2 ? 0 : a + 1, b - 1);
  return dp[a][b] = min(s1 + s2, s2 + s1);
}


bool ok(string a, string b) {
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  return a == b;
}

int main() {
  int T;
  R(T);
  for(int kase = 1; kase <= T; ++kase) {
    int n, r, p, s;
    R(n, r, p, s);
    string a = "";
    REP(i, p) a += 'P';
    REP(i, r) a += 'R';
    REP(i, s) a += 'S';
    string ans = "ZZZ";
    string t = f(0, n);
    if(ok(a, t)) {
      ans = min(ans, t);
    }
    t = f(1, n);
    if(ok(a, t)) {
      ans = min(ans, t);
    }
    t = f(2, n);
    if(ok(a, t)) {
      ans = min(ans, t);
    }
    if(ans[0] == 'Z') ans = "IMPOSSIBLE";
    printf("Case #%d: %s\n", kase, ans.c_str());
  }
  return 0;
}
