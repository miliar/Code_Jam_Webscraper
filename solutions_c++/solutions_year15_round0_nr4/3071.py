#include<bits/stdc++.h>
using namespace std;
int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   int test_case;
   scanf("%d",&test_case);
   int ca=1;
   while(test_case--)
   {
       int x,r,c;
       scanf("%d %d %d",&x,&r,&c);
       printf("Case #%d: ",ca);
        if(x==1)puts("GABRIEL");
       else if(x==2)
       {
           if((r*c)%x!=0)puts("RICHARD");
           else puts("GABRIEL");

       }
       else if(x==3)
       {
           if((r*c)%x || (r*c)==x)puts("RICHARD");
           else puts("GABRIEL");
       }
       else
       {
            if(x==(r*c) || (r*c)%x || (r*c)==8)puts("RICHARD");
             else puts("GABRIEL");
       }
       ca++;
   }
   return 0;
}
