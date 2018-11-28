#include<stdio.h>
int main()
{
    freopen ("a.txt","r",stdin);
    freopen("output.txt","w",stdout);
    long long r,t,n,q=0,sum=0,count;
    scanf("%lld",&n);
    while(n--)
    {
              q++;
              count=0;
              sum=0;
              scanf("%lld %lld",&r,&t);
              sum=(2*r+1);
              count=1;
              
              while(1)
              {
                      
                      r=r+2;    
                      sum+=(2*r+1);
                      if(sum<=t)
                               count++;
                      else
                          break;
                          
              }
              printf("Case #%lld: %lld\n",q,count);    
    }
    return 0;
}
