#include <bits/stdc++.h>
#define ull unsigned long long
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define ins insert
#define mp make_pair
#define iOS ios::sync_with_stdio(false)
ll t,n;
int fq[20];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    for(int k=1;k<=t;k++)
    {
        scanf("%lld",&n);
        int ch=0;
        ll tn=n;
        for(int i=1;i<=1e5;i++)
        {
            ll temp=n;
            while(temp)
            {
                fq[temp%10]++;
                temp/=10;
            }
            int c=1;
            for(int j=0;j<=9;j++)
            {
                if(!fq[j])
                {
                    c=0;
                    break;
                }
            }
            if(c)
            {
                printf("Case #%d: %lld\n",k,n);
                ch=1;
                break;
            }
            n+=tn;
        }
        if(!ch) printf("Case #%d: INSOMNIA\n",k);
        memset(fq,0,sizeof(fq));
    }
}
