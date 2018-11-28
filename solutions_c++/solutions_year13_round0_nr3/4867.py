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
     
     int t,k=0,cases=0,c1,c2;
     long long j,ar[100],a,b;
     //freopen("C-small-attempt0.in","r",stdin);
     //freopen("c.txt","w",stdout);
     for(long long i=1;i<10000001;i++)
     {
             if(ispalindrome(i))
             {
                                //printf("%d\n",i);
                                j=i*i;
                                if(ispalindrome(j))
                                {ar[k++]=j;
                                printf("%lld\n",j);}
             }
     }
    // printf("%d\n",k);
    //for(int i=0;i<k;i++)
    //printf("%lld ",ar[i]);
     scanf("%d",&t);
     while(t--)
     {
               cases++;
               printf("Case #%d: ",cases);
               scanf("%lld%lld",&a,&b);
               if(a>ar[k-1])
               {printf("0\n");continue;}
               if(b>ar[k-1])
               b=ar[k-1];
               for(int i=0;i<k;i++)
               {
                       if(ar[i]>=a)
                       {c1=i;
                       break;}
               }
               for(int i=0;i<k;i++)
               {
                       if(ar[i]<=b)
                       c2=i;
               }
               printf("%d\n",c2-c1+1);        
     
     }
}
