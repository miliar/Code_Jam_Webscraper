#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Aoutputlarge.out","w",stdout);
    long long t,n,m,p,cnt;
    scanf("%lld",&t);
    for(int i=1; i<=t; i++)
    {
        int ans[20]={0};
        cnt=0;
        scanf("%lld",&n);
        int flg=0;
        for(int j=1; j<=100000; j++)
        {
            m=n*j;
            p=m;
            while(m!=0)
            {
                if(ans[m%10]==0)
                    cnt++;
                ans[m%10]=1;
                m/=10;
                if(cnt==10)
                    flg=1;
            }
            if(flg==1)
            {
                printf("Case #%d: %lld\n",i,p);
                break;
            }
        }
        if(flg==0)
            printf("Case #%d: INSOMNIA\n",i);
    }
    return 0;
}
