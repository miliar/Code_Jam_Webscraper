#include <string>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string.h>
#include <utility>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctype.h>
#include <map>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long long LL;

#define FOR(i,n) for(int i = 0;i < n;i++)
#define MP make_pair
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define PII pair<int, int>
#define PLL pair<long long, long long>
#define CLEAR(a) memset(a, 0, sizeof(a))
#define INF 2000000007
#define y1 uu1
#define y2 uu2
#define hash mash
const double EPS = 1E-12;
const double PI = acos(-1.0);
const LL mod = 1000000007;

using namespace std;

int n,r,p,s;

string dp[13][3];
string mg[3] = {"P", "R", "S"};

string get(int lev, int win) {
  if (dp[lev][win] != "") return dp[lev][win];
  if (lev == 0) {
    return mg[win];
  }
  string n1 = get(lev - 1, win);
  string n2 = get(lev - 1, (win+1)%3);

  if (n1 == "Z" || n2 == "Z") {
    dp[lev][win] = "Z";
  } else {
    dp[lev][win] = min(n1,n2) + max(n1,n2);
  }
  return dp[lev][win];
}

void solve() {
  cin >> n >> r >> p >> s;
  string bst = "Z";
  FOR(i, 3) {
    string opt = get(n, i);
    int rr=r,ss=s,pp=p;
    FOR(j, opt.size()) {
      if (opt[j] == 'R') rr--;
      if (opt[j] == 'P') pp--;
      if (opt[j] == 'S') ss--;
    }
    if (rr || pp || ss) continue;
    bst = min(bst, opt);
  }
  if (bst == "Z") {
    cout << "IMPOSSIBLE" << endl;
  } else {
    cout << bst << endl;
  }
}

int main() {
  ios_base::sync_with_stdio(0);
  int tt;
  cin >> tt;

  FOR(t,tt) {
    cout << "Case #" << t+1 << ": ";
    solve();
  }

  return 0;
}
