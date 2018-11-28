#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#define INF 2100000000
using namespace std;
priority_queue<int> s;
int dp[1111][1111], a[1111];
int inf;
int deal(int x, int y){
    if (x <= y) return 0;
    if (dp[x][y] != inf) return dp[x][y];
    for(int i = 1; i < x; i++)
        dp[x][y] = min(dp[x][y], deal(x - i, y) + deal(i, y) + 1);
    return dp[x][y];
}
int main(){
    int T, n, i, j, cas = 0;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin>>T;
    memset(dp, 63, sizeof(dp));
    inf = dp[0][0];
    while(T--){
        scanf("%d", &n);
//        while(!s.empty()) s.pop();
        int ans = 0;
        for(i = 0; i < n; i++){
            int x;
            scanf("%d", &x);
            a[i] = x;
            ans = max(ans, x);
        }
//
        int p = ans;
        int now = 0;
        for(i = p; i >= 1; i--){
            int t = 0;
            for(j = 0; j < n; j++)
                t += deal(a[j], i);
            ans = min(ans, i + t);
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
