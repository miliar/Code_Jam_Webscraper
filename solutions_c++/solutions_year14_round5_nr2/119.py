#include <cstdio>
#include <numeric>
#include <algorithm>
#include <cassert>
#include <cstring>
using namespace std;

int dp[101][10000];

int main()
{
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        int N, P, Q, H[100], G[100], S[100], T[100];
        scanf("%d%d%d", &P, &Q, &N);
        for(int i=0; i<N; i++)
        {
            scanf("%d%d", H+i, G+i);
            T[i]=(H[i]-1)/Q;
            S[i]=(H[i]-Q*T[i]+P-1)/P;
        }
        memset(dp, -1, sizeof dp);
        dp[0][1]=0;
        for(int m=0; m<N; m++)
        {
            for(int s=0; s<10000; s++)
            {
                if(dp[m][s]==-1) continue;
                //kill
                {
                    if(S[m]<=T[m]+s)
                    {
                        int ng=G[m]+dp[m][s];
                        int ns=T[m]+s-S[m];
                        if(dp[m+1][ns]==-1 || dp[m+1][ns]<ng)
                            dp[m+1][ns]=ng;
                    }
                }
                //don't
                {
                    int ng=dp[m][s];
                    int ns=s+T[m]+1;
                    assert(ns<10000);
                    if(dp[m+1][ns]==-1 || dp[m+1][ns]<ng)
                        dp[m+1][ns]=ng;
                }
            }
        }
        int res=0;
        for(int i=0; i<10000; i++)
        {
            res=max(res, dp[N][i]);
        }
        printf("Case #%d: %d\n", t, res);
    }
}
