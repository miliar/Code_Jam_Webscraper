#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <sstream>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cctype>
#include <cassert>
#include <cstring>
// #include <bits/stdc++.h>
using namespace std;

#define REP(i, x, n) for(int i = x; i < (int)(n); i++)
#define rep(i, n) REP(i, 0, n)
#define all(x) (x).begin(), (x).end()
#define F first
#define S second
#define mp make_pair
#define pb push_back

typedef pair<int,int> P;
typedef long long int lli;

// const int INF = (1 << 29);
const double EPS = 1e-9;
const double PI = acos(-1.0);

int card[17];

void solve() {
  vector<int> ans;
  
  rep(i, 17) if(card[i] == 2) {
    ans.push_back(i);
  }

  if(ans.size() == 0) cout << "Volunteer cheated!" << endl;
  else if(ans.size() == 1) cout << ans[0] << endl;
  else cout << "Bad magician!" << endl;
}

void input() {
  memset(card, 0, sizeof(card));
  int n;
  
  cin >> n;
  n--;

  rep(i, 4) rep(j, 4) {
    int tmp;
    cin >> tmp;
    if(i == n) card[tmp]++;
  }
  
  cin >> n;
  n--;
  
  rep(i, 4) rep(j, 4) {
    int tmp;
    cin >> tmp;
    if(i == n) card[tmp]++;
  }
}

int main() {
  // ios_base::sync_with_stdio(false);
  
  int T;
  cin >> T;
  for(int tc = 1; tc <= T; tc++) {
    input();
    cout << "Case #" << tc << ": ";
    solve();
  }

  return 0;
}
