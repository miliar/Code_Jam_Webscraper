#include<iostream>
#include<stdio.h>
#define LL long long
using namespace std;

int main()
{
    LL r,p,ans,i,count,t,k,j;
    scanf("%lld",&t);
    for(k=1;k<=t;k++)
    {
       // printf("%d\n",k);
        scanf("%lld %lld",&r,&p);
        count=0;
        i=1;
        while(p > 0)
        {

            ans=(r+i)*(r+i) - (r+i-1)*(r+i-1);
            //printf("%lld %lld\n",p,ans);
            if(ans <= p)
            {
                p=p-ans;
                count++;
            }
            else
                break;
            i++;
            i++;
        }
        printf("Case #%lld: %lld\n",k,count);
    }
    return 0;
}
