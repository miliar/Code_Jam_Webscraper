#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <cstring>
#include <iomanip>
#include <cctype>
#include <map>

using namespace std;

int dp1[1005][1005];
int dp[1005][1005];

void solve(int t) {
    int n; cin>>n;
    vector<int> v(n);
    for(int i = 0;i < n;i++) {
        cin>>v[i];
    }
    sort(v.begin(),v.end());
    for(int i = 0;i <= 1000;i++) {
        dp[0][i] = dp1[v[0]][i];
    }
    for(int i = 1;i < n;i++) {
        dp[i][0] = v[i];
        for(int j = 1;j <= 1000;j++) {
            dp[i][j] = dp[i][j - 1];
            for(int k = 0;k <= min(j,v[i]);k++) {
                dp[i][j] = min(dp[i][j],max(dp[i - 1][j - k] + k,dp1[v[i]][k] + (j - k)));
            }
        }
    }
    printf("Case #%d: %d\n",t,dp[n - 1][1000]);
}

int main() {
    freopen("/Users/administrator/Desktop/B-small-attempt2.in","r",stdin);
    freopen("/Users/administrator/Desktop/gcjoutput2.txt","w",stdout);
    for(int i = 1;i <= 1000;i++) {
        dp1[i][0] = i;
    }
    for(int j = 1;j <= 1000;j++) {
        for(int i = 1;i <= 1000;i++) {
            dp1[i][j] = dp1[i][j - 1];
            for(int k = 1;k <= (i - 1);k++) {
                dp1[i][j] = min(dp1[i][j],max(dp1[i - k][j - 1] + 1,k + j));
            }
        }
    }
    int t; cin>>t;
    for(int i = 1;i <= t;i++) {
        solve(i);
    }

}