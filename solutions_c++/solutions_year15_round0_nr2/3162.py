#include<bits/stdc++.h>
using namespace std;

const int N = 1003;
int a[N],b[N],dp[N][N];

int f(int sum,int eat)
{
    if(dp[sum][eat]!=-1)return dp[sum][eat];
    if(sum<=eat)return dp[sum][eat]=0;
    dp[sum][eat]=1+ f(sum/2,eat) +f( sum-sum/2,eat );
    return dp[sum][eat];
}

int main()
{
   // freopen("Pancake.old.txt","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("b-large.out","w",stdout);

    int T,i,j,k,n,m,cs=0,val,split,cnt=0;
    cin>>T;

   // memset(dp,-1,sizeof(dp));

    for(cs=1;cs<=T;cs++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)scanf("%d",&a[i]);
        m=N;
        for(i=1;i<N;i++)    ///  height of the maximum tower
        {
            k=i;
            split=0;
            cnt=0;
            for(j=0;j<n;j++)
            {
                cnt+=a[j]/i;
                if( a[j]%i==0 )cnt--;
                split=max(cnt,split);
            }
            k+=split;
            m=min( k,m );

          //  if(k==4)cout<<i<<endl;
        }
        printf("Case #%d: %d\n",cs,m);
    }

    return 0;
}
