#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<limits.h>
#include<map>
#include<queue>
#include<vector>
using namespace std;

long long reverse(long long x)
{
     long long r=0,d;
     while(x>0)
     {
               d=x%10;
               r=r*10+d;
               x=x/10;
     }
     return r;
}
     
bool ispalindrome(long long x)
{
     long long y=reverse(x);
     if(x==y)
     return 1;
     return 0;
}
int main()
{
     
     int t,cases=0,x,y,k=0;
     long long j,ar[100],a,b;
     for(long long i=1;i<10000001;i++)
     {
             if(ispalindrome(i))
             {
                                //printf("%d\n",i);
                                j=i*i;
                                if(ispalindrome(j))
                                ar[k++]=j;
                                //printf("%lld\n",j);}
             }
     }
    // printf("%d\n",k);
    //for(int i=0;i<k;i++)
    //printf("%lld ",ar[i]);
     freopen("C-small-attempt3.in","r",stdin);
     freopen("e.txt","w",stdout);
     scanf("%d",&t);
     while(t--)
     {
               cases++;
               printf("Case #%d: ",cases);
               scanf("%lld%lld",&a,&b);
               if(a>484)
               {printf("0\n");continue;}
               if(b>484)
               b=484;
               for(int i=0;i<k;i++)
               {
                       if(a<=ar[i])
                       {x=i;
                       break;}
               }
               for(int i=0;i<k;i++)
               {
                       if(b>=ar[i])
                       y=i;
               }
               //printf("x=%d y=%d\n",x,y);
               printf("%d\n",y-x+1);        
     
     }
}
