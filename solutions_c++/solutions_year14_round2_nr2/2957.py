#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;



int main()
{
    long long x=0,a,b,k,t,count=0;
    long long i,j;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld %lld %lld",&a,&b,&k);
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                if((i & j) < k)
                        count++;
                else
                    continue;
            }
        }
        printf("Case #%lld: %lld\n",++x,count);
        count=0;
    }
}
