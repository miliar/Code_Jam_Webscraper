#include<stdio.h>
int main()
{
    freopen("D-small-attempt0.in","r",stdin); freopen("gcjdout.txt","w",stdout);
    long long int T,t,min,x,c,r,b,ans;
    scanf("%lld",&T);
    for(t=1;t<=T;t++)
    {
                     scanf("%lld %lld %lld",&x,&r,&c);
                     b=r*c;
                     min=r;
                     if(c<r)
                     min=c;
                     if(x==1)
                     {
                             ans=1;
                     }
                     else if(x==2)
                     {
                          if(b%2==0)
                          ans=1;
                          else
                          ans=2;
                     }
                     else if(x==3)
                     {
                          if(min==1)
                          {
                                    ans=2;
                          }
                          else
                          {
                              if(b%3==0)
                              {
                                        ans=1;
                              }
                              else
                              {
                                  ans=2;
                              }
                          }
                     }
                     else if(x==4)
                     {
                         if(min==1)
                         {
                                   ans=2;
                         }
                         else
                         {
                             if(b>8&b%4==0)
                             {
                                           ans=1;
                             }
                             else
                             {
                                 ans=2;
                             }
                         }
                     }
                     printf("Case #%lld: ",t);
                     if(ans==1)
                     printf("GABRIEL\n");
                     else
                     printf("RICHARD\n");
    }
}
                          
