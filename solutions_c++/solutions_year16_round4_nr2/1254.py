#include <bits/stdc++.h>

using namespace std;
double dp[210][210];
double oP[210];
double sol=0.0f;
vector<double> unP;
int n,k;
double doThis(int k)
{
    dp[0][0]=1.0;
    for(int i=1; i<=k; i++)
    {
        for(int j=0; j<=i; j++)
            dp[i][j]=dp[i-1][j]*(1-oP[i])+(j>0?dp[i-1][j-1]*oP[i]:0);
    }
    return dp[k][k/2];
}
void seT(int idx,int kk)
{
    if(idx==n&&k==kk)
    {
    /*    printf("LLA ");
        for(int i=1;i<=k;i++)
        {
            printf("%lf ",oP[i]);

        }
        printf("\n");
      */  sol=max(sol,doThis(k));
    }
    if(idx==n)return;
    seT(idx+1,kk);
    oP[kk+1]=unP[idx];
    seT(idx+1,kk+1);
}

bool cmp(double a,double b)
{
    return abs(a-0.5f)<abs(b-0.5f);
}
int main()
{
    int t,caseno=1;
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&k);
        unP.clear();
        for(int i=0; i<n; i++)
        {
            double p;
            scanf("%lf",&p);
            unP.push_back(p);
        }
        sort(unP.begin(),unP.end());
        int curr=0;
        sol=0;
        seT(0,0);
        printf("Case #%d: %.10lf\n",caseno++,sol);
    }
    return 0;
}
