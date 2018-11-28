/*
 *
 * Tag: Implementation
 * Time: O(n)
 * Space: O(n)
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;
const int N = 350;
const int M = 30110;
const long long MOD = 1000000007;
const double eps = 1e-10;


int main() {
    freopen("/Users/ybc/Project/CCPP/ACM/D-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/ybc/Project/CCPP/ACM/out.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    for (int cas = 1; cas <= T; ++ cas) {
        printf("Case #%d: ",cas);
        int n;
        scanf("%d",&n);
        int dp[2][n], rec[2][n];
        vector<int> arr(n);
        for(int i = 0; i < n; i ++)
            scanf("%d",&arr[i]);
        //      for(int i = 0; i < n; i ++)
        //          printf("~ %d\n",arr[i]);
        dp[0][0] = dp[1][0] = 0;
        for(int i = 0; i < n; i ++){
            rec[0][i] = 1;
            rec[1][i] = arr[i];
            dp[0][i] = dp[1][i] = 0;
        }
        for(int i = 1; i < n; i ++){
            for(int j = 0; j < 2; j ++){
                int sumup = 0, sumdwn = 0;
                sumup = rec[j][i] - rec[0][i - 1];
                sumdwn = rec[j][i] - rec[1][i - 1];
                if(sumup < 0)
                    sumup *= -1;
                if(sumdwn < 0)
                    sumdwn *= -1;
                //        printf("%d %d\n",sumup,sumdwn);
                dp[j][i] = max(sumup + dp[0][i - 1], sumdwn + dp[1][i - 1]);
            }
        }
        //     for(int i = 0; i < n; i ++)
        //         printf("%d %d\n",dp[0][i],dp[1][i]);
        printf("%d\n",max(dp[0][n-1],dp[1][n-1]));
    }
    return 0;
}
