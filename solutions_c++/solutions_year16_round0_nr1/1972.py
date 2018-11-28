//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

long long ar[12];

int main()
{
    freopen("out.txt","rt",stdin);
    freopen("out1.txt","wt",stdout);
    long long i,j,k,l,n,cas,test,flag,temp,now,ans=0;

    cin>>test;
    for(cas=1;cas<=test;cas++)
    {
        scanf("%lld",&n);

        memset(ar,0,sizeof(ar));

        temp=0;
        for(i=1;i<=100000;i++)
        {
            temp+=n;
            now=temp;
            while(now)
            {
                ar[now%10]=1;
                now/=10;
            }

            flag=1;
            for(j=0;j<10;j++)
            {
                if(ar[j]==0)
                {
                    flag=0;
                    break;
                }
            }

            if(flag) break;
        }

        if(flag) ans=max(ans,i);

        if(flag) printf("Case #%lld: %lld\n",cas,i*n);
        else printf("Case #%lld: INSOMNIA\n",cas);

    }



}
