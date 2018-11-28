#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<limits.h>
#include<map>
#include<queue>
#include<vector>
using namespace std;
int main()
{
     int t,ar[5]={1,4,9,121,484},a,b,c1,c2,cases=0;
     freopen("C-small-attempt0.in","r",stdin);
     freopen("c.txt","w",stdout);
     scanf("%d",&t);
     while(t--)
     {
               cases++;
               printf("Case #%d: ",cases);
               scanf("%d%d",&a,&b);
               if(a>484)
               {printf("0\n");continue;}
               if(b>484)
               b=484;
               for(int i=0;i<5;i++)
               {
                       if(ar[i]>=a)
                       {c1=i;
                       break;}
               }
               for(int i=0;i<5;i++)
               {
                       if(ar[i]<=b)
                       c2=i;
               }
               printf("%d\n",c2-c1+1);
     }
}
