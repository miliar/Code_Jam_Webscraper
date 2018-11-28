#include<iostream>
#include<stdio.h>
using namespace std;
int ar[11];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.in", "w", stdout);
    int t,k=1;
    scanf("%d",&t);
    while(t--)
    {
       int m,n,i,j;
       long long int r=2;
       scanf("%d",&n);
       if(n==0)
       printf("Case #%d: INSOMNIA\n",k);
       else
       {
              m=n;
              for(i=0;i<=9;i++)
              ar[i]=0;
              while(1)
              {
                int flag=0;
                while(m>=1)
                {
                 ar[m%10]++;
                 m=m/10;
                }
                for(i=0;i<=9;i++)
                {
                   if(ar[i]==0)
                   flag=1;
                }
                if(flag==0)
                break;
                else
                m=n*r;
                r++;
              }
              printf("Case #%d: %lld\n",k,n*(r-1));
       }
       k++;
    }
    return 0;
}
              
