//#include<bits/stdc++.h>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
//#define LOCAL
using namespace std;
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
#define clean(n,val) memset((n),(val),sizeof(n))
#define MP make_pair
#define PB push_back
#define ll long long
#define debug(x) x
typedef pair<int, int> PI;
const int INF = 0xFFFFFFF;
const int MOD = 1e9+7;
const int MAXN = 100005;

vector<char> res;


void solve(char s[]) {
  int dp[1005][50] = {0};
  int has[1005] = {0};
  int len = strlen(s);
  dp[0][s[0] - 'A'] = 1;
  for ( int i = 1 ; i < len ; i++ ) {
    for ( int j = 0; j < 26 ; j++ ) {
      dp[i][j] += dp[i - 1][j] + (s[i] - 'A' == j);
    }
  }

  int now = 25;
  for ( int i = len - 1 ; i >= 0 ; i-- ) {
    while ( dp[i][now] <= 0 ) now--;
    if ( s[i] - 'A' == now ) res.PB(s[i]), has[i] = 1;
  }

  for ( int i = 0 ; i < len ; i++ ) {
    if (!has[i] ) res.PB(s[i]);
  }


}

int main() {
  int T, kase = 1;
  #ifdef LOCAL
    freopen("input1.txt", "r", stdin);
    freopen("output1.txt", "w", stdout);
  #endif

  cin >> T;
  while ( T-- ) {
    char s[1500];
    cin >> s;
    res.clear();
    //memset(res, 0, sizeof(res));
    solve(s);
    cout << "Case #" << kase++ << ": ";
    for ( auto it : res) cout << it;
    cout << endl;
  }


  return 0;
}
