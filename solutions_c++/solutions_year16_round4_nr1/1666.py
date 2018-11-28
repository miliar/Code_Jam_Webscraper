#include <bits/stdc++.h>
#define maxx 100005
#define inf 2000000000
#define mod 1000000007
#define pii pair<int,int>
#define piii pair<pii,pii>
#define pli pair<long long,int>
#define f first
#define s second
#define in(x) scanf("%d",&x)
#define IN(x) scanf("%lld",&x)
#define inch(x) scanf("%s",x)
#define indo(x) scanf("%lf",&x)
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int t, n, p, r, s;
int dp[3][(1<<13)][13];

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    in(t);
    for(int cases = 1; cases <= t; cases ++){
        in(n); in(r); in(p); in(s);
        printf("Case #%d: ",cases);

        for(int i = 1; i <= 3; i++){
            dp[i][0][1] = i;
            for(int j = 0; j < n; j++){
                for(int k = 1; k <= (1<<j); k++){
                    if(dp[i][j][k] == 1){
                        dp[i][j + 1][2*k - 1] = 1;
                        dp[i][j + 1][2*k] = 2;
                    }
                    else if(dp[i][j][k] == 2){
                        dp[i][j + 1][2*k - 1] = 2;
                        dp[i][j + 1][2*k] = 3;
                    }
                    else{
                        dp[i][j + 1][2*k - 1] = 1;
                        dp[i][j + 1][2*k] = 3;
                    }
                }
            }
        }
        int P, R, S;
        for(int i = 1; i <= 3; i++){
            P = 0, R = 0, S = 0;
            for(int j = 1; j <= (1<<n); j++){
                if(dp[i][n][j] == 1)
                    P++;
                else if(dp[i][n][j] == 2)
                        R++;
                else
                    S++;
            }
            if(P == p && R == r && S == s){
                for(int j = 1; j < n; j++){
                    for(int l = 1; l <= n - j; l++){
                    int change = 0;
                    for(int k = 2*(l - 1)*(1<<j) + 1; k <= 2*(l - 1)*(1<<j) + (1<<j); k++){
                        if(dp[i][n][k] < dp[i][n][k + (1<<j)]){
                            break;
                        }
                        if(dp[i][n][k] > dp[i][n][k + (1<<j)]){
                            change = 1;
                            break;
                        }
                    }
                    if(change){
                        for(int k = 2*(l - 1)*(1<<j) + 1; k <= 2*(l - 1)*(1<<j) + (1<<j); k++){
                            swap(dp[i][n][k], dp[i][n][k + (1<<j)]);
                        }
                    }
                    }
                }
                for(int j = 1; j <= (1<<n); j++){
                    if(dp[i][n][j] == 1){
                        printf("P");
                    }
                    else if(dp[i][n][j] == 2)
                        printf("R");
                    else
                        printf("S");
                }
                printf("\n");
                break;
            }
        }
        if(P == p && R == r && S == s)
            continue;
        puts("IMPOSSIBLE");
    }
    return 0;
}
