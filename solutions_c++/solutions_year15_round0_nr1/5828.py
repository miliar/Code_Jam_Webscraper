#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin); freopen("gcjalargeout.txt","w",stdout);
    long long int T,t,ans,stand,a[2000],i,s,need;
    char str[2000];
    scanf("%lld",&T);
    for(t=1;t<=T;t++)
    {
                     scanf("%lld",&s);
                     scanf("%s",str);
                     for(i=0;i<=s;i++)
                     {
                                      a[i]=str[i]-'0';
                     }
                     ans=0;
                     stand=0;
                     for(i=0;i<=s;i++)
                     {
                                      if(a[i]==0)
                                      {
                                                 continue;
                                      }
                                      else
                                      {
                                          if(stand>=i)
                                          {
                                                      stand=stand+a[i];
                                          }
                                          else
                                          {
                                              need=i-stand;
                                              ans=ans+need;
                                              stand=stand+need+a[i];
                                          }
                                      }
                     }
                     printf("Case #%lld: %lld\n",t,ans);
    }
    return 0;
}   
