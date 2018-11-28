#include <bits/stdc++.h>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)
#define FORD(i,b,e) for(int i=(b); i >= (e); --i)
#define REP(i,n) for(int i=0; i < (n); ++i)
#define SIZE(c) (int) (c).size()
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
#define FWD(i,a,b) for (int i=(a); i<(b); ++i)
#define BCK(i,a,b) for (int i=(a); i>(b); --i)
#define PI acos(-1.0)
#define pb push_back
#define mp make_pair
#define st first
#define nd second

using namespace std;

typedef long long int LLI;
typedef pair < int , int > PII;
typedef pair < LLI , LLI > PLL;

typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < PII > VP;
typedef vector < LLI > VL;
typedef vector < PLL > VPL;

typedef vector < VI > VVI;
typedef vector < VL > VVL;
typedef vector < VB > VVB;
typedef vector < VP > VVP;

string bestSol(int r, int p, int s) {
  if (r + p + s == 1) {
    if (r == 1) {
      return "R";
    }
    if (p == 1) {
      return "P";
    }
    if (s == 1) {
      return "S";
    }
  }

  int np = (p + r - s);
  int nr = (r + s - p);
  int ns = (s + p - r);
  if (min({np, nr, ns}) < 0) return "";
  if (np % 2 == 1 || nr % 2 == 1 || ns % 2 == 1) return "";

  auto str = bestSol(nr/2, np/2, ns/2);
  string ans = "";
  for (char c : str) {
    if (c == 'P') ans += "PR";
    if (c == 'R') ans += "RS";
    if (c == 'S') ans += "PS";
  }
  return ans;
}

string enhance(const string& s) {
  int len = SIZE(s);
  if (len == 1) return s;
  auto p1 = enhance(s.substr(0, len/2));
  auto p2 = enhance(s.substr(len/2, len/2));
  if (p1 < p2) return p1 + p2;
  return p2 + p1;
}

int main() {
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  FOR(i, 1, t) {
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    cout << "Case #" << i << ": ";
    auto ans = bestSol(r, p, s);
    if (ans == "") {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << enhance(ans) << '\n';
    }
  }
}
