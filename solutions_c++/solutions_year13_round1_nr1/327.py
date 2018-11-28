#include<iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<set>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
    freopen("reada.txt","r",stdin);
    freopen("outa.txt","w",stdout);
    long long int r,b,mid,one=1,two=2,ans,high,low;
    double val,temp,d1,d2,d3;
    int i,t;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%lld%lld",&r,&b);
        temp=b;
        d2=r;
        high=sqrt(b)+one;
        low=one;
//        printf("%lld %lld\n",high,low);
        while(high>low)
        {
            mid=(high+low)/2;
            d1=mid;
            val=d1*(2.0*d2+2.0*d1-1.0); 
            //ans=mid*(two*r+two*mid-one);
          //  printf("%lld %lf %lf\n",mid,val,temp);
            if(val>temp)
               high=mid;
            else
               low=mid+1;
        }
        for(mid=mid-two;  ;mid++)
        {
           ans=mid*(two*r+two*mid-one);
           if(ans>b) break;
        }
        printf("Case #%d: %lld\n",i,mid-one);
    }
    return 0;
}
