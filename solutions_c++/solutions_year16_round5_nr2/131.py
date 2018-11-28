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

string getString(int n, const VI& father, const VVI& chld, const VI& siz, const string& names) {
  string res = "";
  VI cands;
  REP(i, n) if (father[i] == -1) cands.pb(i);
  while (!cands.empty()) {
    int rndMax = 0;
    for (int u : cands) rndMax += siz[u];

    int rnd = (rand() % rndMax);

    REP(i, SIZE(cands)) {
      if (rnd < siz[cands[i]]) {
        rnd = i;
        break;
      } else {
        rnd -= siz[cands[i]];
      }
    }

    int x = cands[rnd];
    res += names[x];
    swap(cands[rnd], cands[SIZE(cands)-1]);
    cands.pop_back();
    for (int u : chld[x]) cands.pb(u);
  }
  return res;
}

void dfs(int x, const VVI& chld, VI& siz) {
  siz[x] = 1;
  for (int u : chld[x]) {dfs(u, chld, siz); siz[x] += siz[u];}
}

int main() {
  ios_base::sync_with_stdio(0);

  srand(time(0));

  cout << fixed << setprecision(4);

  int T;
  cin >> T;
  FOR(i, 1, T) {
    cout << "Case #" << i << ": ";

    int n;
    cin >> n;

    VI father(n);
    VVI chld(n);
    VI siz(n);

    REP(i, n) {
      int a;
      cin >> a;
      a--;
      father[i] = a;
      if (a != -1) {
        chld[a].pb(i);
      }
    }

    REP(i, n) if (father[i] == -1) dfs(i, chld, siz);

    string names;
    cin >> names;

    int numWords;
    cin >> numWords;

    REP(_, numWords) {
      string s;
      cin >> s;

      if (SIZE(s) > n) { cout << "0.0 "; continue; }

      const int TIMES = 3e4;
      int ok = 0;

      REP(__, TIMES) {
        string r = getString(n, father, chld, siz, names);
        if (r.find(s) != string::npos) ok++;
      }

      cout << (1. * ok / TIMES) << ' ';
    }

  cout << '\n';  

  }
  
  return 0;
}

/*************************************************************************/
