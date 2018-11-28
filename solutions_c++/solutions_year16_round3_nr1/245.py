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

typedef pair <int, char> party;

int main() {
  ios_base::sync_with_stdio(0);

  int T;
  cin >> T;
  FOR(cas, 1, T) {
    cout << "Case #" << cas << ": ";
    int n;
    cin >> n;
    vector<party> parties(n);
    REP(i, n) cin >> parties[i].st;
    REP(i, n) parties[i].nd = 'A' + i;
    sort(ALL(parties));
    while (parties.back().st) {
      if (n >= 3 && parties[n-1].st == 1 && parties[n-3].st == 1) {
        cout << parties[n-1].nd << ' ';
        parties[n-1].st--;
      } else {
        cout << parties[n-2].nd << parties[n-1].nd << ' ';
        parties[n-2].st--; parties[n-1].st--;
      }
      sort(ALL(parties));
    }
    cout << '\n';
  }
  

  return 0;
}

/*************************************************************************/
