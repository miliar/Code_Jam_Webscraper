#include <bits/stdc++.h>
using namespace std;
int check(long long x[])
{
    for(int i=0;i<10;++i)
    {
        if(!x[i])return 1;
    }
    return 0;
}
int main()
{
    int t;cin>>t;
    for(int k=1;k<=t;++k)
    {
        long long i=1,p,n,x[10]={0};
        scanf("%lld",&n);
        printf("Case #%d: ",k);
        if(!n){printf("INSOMNIA\n");continue;}
        do
        {
            p=(i++)*n;
            while(p)
            {
                x[p%10]++;
                p/=10;
            }
        }while(check(x));
        printf("%d\n",(--i)*n);
    }
    return 0;
}
