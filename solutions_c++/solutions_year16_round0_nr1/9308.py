#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    long long n,tc=0,ar[10],a,b,t,i,c,m;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld",&n);
        if(n==0) {printf("Case #%lld: INSOMNIA\n",++tc);continue;}
        for(i=0;i<10;i++)
        {
            ar[i]=0;
        }
        c=0;
        m=1;
        while(c!=10)
        {
            a=n*m;
            b=a;
            while(a)
            {
                if(ar[a%10]==0)
                {
                    ar[a%10]=1;
                    c++;
                }
                a/=10;
            }
            m++;
        }
        printf("Case #%lld: %lld\n",++tc,b);
    }
}
