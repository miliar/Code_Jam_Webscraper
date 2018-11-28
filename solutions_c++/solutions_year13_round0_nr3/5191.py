#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    int a,b,t,c,q,i,s,r;
    scanf("%d",&t);
    for(q=1;q<=t;q++)
    {    
        s=0;
         int P[7] = {1,4,9,121,484};
        scanf("%d%d",&a,&b);
        P[5]=a,P[6] =b;
        sort(P,P+7);
   //     for(i=0;i<7;i++)
      //  printf(" %d",P[i]);
        r=s=-1;        
        for(i=0;i<7;i++)
        if(P[i]==a && r==-1)
        r=i;
        
        for(i=6;i>=0;i--)
        if(P[i]==b && s==-1)
         s=i;
        
        
        printf("Case #%d: %d\n",q,s-r-1);
          
     }
   //  system("pause");
     return 0;
 }        
             
