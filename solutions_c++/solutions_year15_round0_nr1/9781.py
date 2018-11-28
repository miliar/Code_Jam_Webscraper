#include<cstdio>
#include<iostream>

using namespace std;

int main()
{
    long long int t,T,sm,k,s[1001],i,sum,req;
    scanf("%lld",&T);
    for(t=1;t<=T;t++)
    {
        req=0;
        scanf("%lld %lld",&sm,&k);
        for(i=sm;i>=0;i--)
        {
            s[i]=k%10;
            k/=10;
        }
        sum=s[0];
        for(i=1;i<=sm;i++)
        {
            if(sum>=i)
                sum+=s[i];
            else
            {
                req+=i-sum;
                sum+=i-sum+s[i];
            }
        }
        printf("Case #%lld: %lld\n",t,req);
    }
    return 0;
}
