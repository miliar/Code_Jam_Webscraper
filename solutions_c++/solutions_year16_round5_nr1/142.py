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

typedef long double K;

/*************************************************************************/

int main() {
  ios_base::sync_with_stdio(0);

  int T;
  cin >> T;
  FOR(i, 1, T) {
    cout << "Case #" << i << ": ";
    string s;
    cin >> s;

    int ans = 0;

    while (true) {
      if (s == "") break;

      bool found = false;

      REP(i, SIZE(s) - 1) if (s[i] == s[i + 1]) {
        string ns = "";
        if (i > 0) ns = s.substr(0, i);
        if (i + 1 < SIZE(s) - 1) ns += s.substr(i + 2);
        ans += 10;
        s = ns;
        found = true;
        break;
      }

      if (found) continue;

      ans += SIZE(s) / 2 * 5;
      break;
    }

    cout << ans << '\n';
  }
  
  return 0;
}

/*************************************************************************/
