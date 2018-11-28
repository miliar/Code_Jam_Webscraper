#include <bits/stdc++.h>

using namespace std;

int N, K;
double P[200];
double dp[205][205];

void _main(int TEST)
{
    scanf("%d%d", &N, &K);
    vector<double> A;
    double x;
    for(int i=0; i<N; i++)
    {
        scanf("%lf", &x);
        A.push_back(x);
    }
    sort(A.begin(), A.end());
    double ans=0.0;
    for(int t=0; t<N; t++)
    {
        for(int i=0; i<K; i++)
            P[i]=A[(t+i)%N];
        for(int i=0; i<=K; i++)
            for(int j=0; j<=K; j++)
                dp[i][j]=0.0;
        dp[0][0]=1.0;
        for(int i=0; i<K; i++)
        {
            double p_yes=P[i];
            double p_no=1.0-P[i];
            for(int j=0; j<=i; j++)
            {
                dp[i+1][j+1]+=p_yes*dp[i][j];
                dp[i+1][j]+=p_no*dp[i][j];
            }
        }
        ans=max(ans, dp[K][K/2]);
    }
    printf("%.9f\n", ans);
}

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        printf("Case #%d: ", i);
        _main(i);
    }
    return 0;
}
