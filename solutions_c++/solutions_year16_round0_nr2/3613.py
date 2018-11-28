// Tapan Sahni
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <iomanip>
#include <map>
#include <complex>
#include <set>

using namespace std;
typedef long long LL;
typedef pair <int, int> PII;

const int N = 1e5 + 10;
const LL mod = 1000000007;

int dp[222][3];
void solve() {
  int t, tNum = 1; 
  cin >> t;
  while(t--) {
    string str;
    cin >> str;
    int n = str.length();
    memset(dp, 0, sizeof dp);
    if(str[0] == '-') {
      dp[0][0] = 0;
      dp[0][1] = 1;
    }
    else {
      dp[0][0] = 1;
      dp[0][1] = 0;
    }
    for(int i = 1; i < n; i++) {
      if(str[i] == '-') {
        dp[i][0] = dp[i - 1][0];
        dp[i][1] = dp[i][0] + 1;
      }
      else {
        dp[i][1] = dp[i - 1][1];
        dp[i][0] = dp[i][1] + 1;
      }
    }
    cout << "Case #" << tNum << ": " << dp[n - 1][1] << endl; 
    tNum++;
  }
  return; 
}
int main() {
    ios::sync_with_stdio(false) ; cin.tie(nullptr);
    solve();
    return  0;
}
// Never Quit
