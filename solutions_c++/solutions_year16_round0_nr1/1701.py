#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll dp[1000111];
int c[10];
int main()
{
    freopen("1.in","r",stdin);
    freopen("1-out.txt","w",stdout);
    int t,cs=1;
    ll i,j,k;
    for(i=1;i<=1000000;i++)
    {
        for(j=0;j<=9;j++)
            c[j]=0;
        for(j=i;;j+=i)
        {
            k=j;
            while(k>0)
            {
                c[k%10]=1;
                k/=10;
            }
            for(k=0;k<=9;k++)
                if(c[k]==0)
                    break;
            if(k==10)
                break;
        }
        dp[i]=j;
    }
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        if(n==0)
            printf("Case #%d: INSOMNIA\n",cs);
        else
            printf("Case #%d: %lld\n",cs,dp[n]);
        cs++;
    }
    return 0;
}
