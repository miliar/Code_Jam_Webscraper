#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;

int T,N,K;
double P[205];
double D[205];
double dp[202][102];

double f()
{
    int H = K/2;
    memset(dp,0,sizeof(dp));
    dp[0][0] = 1.0;
    for(int i=0;i<K;i++) {
        for(int j=0;(j<=i) && (j<=H);j++) {
            dp[i+1][j+1] += (dp[i][j]*D[i+1]);
            dp[i+1][j] += (dp[i][j]*(1.0-D[i+1]));
        }
    }
    return dp[K][H];
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++) {
        cin>>N>>K;
        for(int i=1;i<=N;i++) cin>>P[i];
        cout<<"Case #"<<ca<<": ";
        sort(P+1,P+N+1);
        double ans = 0.0;
        if(N == K) {
            for(int i=1;i<=N;i++) D[i] = P[i];
            ans = max(ans,f());
        } else {
            int u = N-K;
            for(int i=1;i<=(N-u+1);i++) {
                int pos = 0;
                for(int j=1;j<=N;j++) {
                    if((j>=i) && (j<=(i+u-1))) continue;
                    pos++;
                    D[pos] = P[j];
                }
                ans =max(ans,f());
            }
        }
        printf("%.15lf\n",ans);
    }
    return 0;
}
