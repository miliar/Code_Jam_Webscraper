#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<iomanip>
#include<algorithm>
using namespace std;
typedef long double ldb;
ldb pp[205],dp[205][205];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        int n,k;
        cin>>n>>k;
        for(int i=0;i<n;i++)
            cin>>pp[i];
        sort(pp,pp+n);
        ldb res=0;
        for(int i=0;i<=k;i++)
        {
            memset(dp,0,sizeof(dp));
            dp[0][0]=1;
            int t=0;
            for(int j=0;j<i;j++)
            {
                t++;
                for(int p=0;p<=k;p++)
                {
                    dp[t][p]+=dp[t-1][p]*(1-pp[j]);
                    if(p>0)dp[t][p]+=dp[t-1][p-1]*pp[j];
                }
            }
            for(int j=n-1;t<k;j--)
            {
                t++;
                for(int p=0;p<=k;p++)
                {
                    dp[t][p]+=dp[t-1][p]*(1-pp[j]);
                    if(p>0)dp[t][p]+=dp[t-1][p-1]*pp[j];
                }
            }
            res=max(res,dp[k][k/2]);
        }
        cout<<"Case #"<<ca<<": "<<fixed<<setprecision(10)<<res<<endl;
    }
    return 0;
}
