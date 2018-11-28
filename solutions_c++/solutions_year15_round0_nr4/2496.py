#include <iostream>
#include <queue>
#include <cstdio>
using namespace std;
char *name[]={"GABRIEL", "RICHARD"};

int main ()
{
    freopen ("D-small-attempt0.in","r",stdin);
    freopen ("D_output.txt","w",stdout);
    int t,cas=0;
    int x,r,c;
    scanf("%d",&t);
    while(cas++<t)
    {
         int ans = 0;
         scanf("%d%d%d",&x,&r,&c);
         if(x==1)ans=0;
         else if((r*c)%x!=0)ans=1;
         else if(x==2)ans=0;
         else if(r*c==x)ans=1;
         else if(x*(x-1)<=r*c)ans=0;
         else ans=1;//simple
         printf("Case #%d: %s\n",cas,name[ans]);
    }

  return 0;
}
