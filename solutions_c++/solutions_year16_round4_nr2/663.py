
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std ; 

typedef long long ll ; 

double prob[222] ; 
 
double dp[222][222] ; 
void sol(){
    memset(dp, 0, sizeof(dp)) ; 
    int N, K ; 
    scanf("%d%d", &N, &K) ; 
    for(int i = 1 ; i <= N ; i++)
        scanf("%lf", prob+i) ; 
    sort(prob+1, prob+N+1) ; 
    double ans = 0 ; 
    for(int k = 0 ; k <= K ; k++){  
        vector<double> ps ; 
        for(int i = 1 ; i <= k ; i++)
            ps.push_back(prob[i]) ; 
        for(int i = N ; i >= N-(K-k)+1 ; i--)
            ps.push_back(prob[i]) ; 
        memset(dp, 0, sizeof(dp)) ; 
        dp[0][0] = 1. ; 
        for(int i = 1 ; i <= ps.size() ; i++){
            for(int y = 0 ; y <= ps.size() ; y++){
                if(y)
                    dp[i][y] = dp[i-1][y-1]*ps[i-1] + dp[i-1][y]*(1-ps[i-1]) ; 
                else
                    dp[i][y] = dp[i-1][y]*(1-ps[i-1]) ; 
            }
        }
        ans = max(ans, dp[ps.size()][K/2]) ; 
    }
    printf("%.10f\n", ans) ; 
}

int main()
{
    int T ; 
    scanf("%d", &T) ; 
    for(int time = 1 ; time <= T ; time++){
        fprintf(stderr, "solving case (%d / %d)...\n", time, T) ; 
        printf("Case #%d: ", time) ; 
        sol() ; 
    }
    return 0 ; 
}


