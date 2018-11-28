#include <iostream>
#include <cstdio>

using namespace std;
int main()
{
      freopen("A-small-attempt2.in","r",stdin);
    freopen("ankita.txt","w",stdout);
    int t,r,t1,count;
    scanf("%d",&t);
    int a=1;
    while(t--)
    {
    scanf("%d",&r);
    scanf("%d",&t1);
    count=0;
    while(t1>0)
    {
     if(t1-(((r+1)*(r+1))-(r*r))>=0)
     count++;
     t1=t1-(((r+1)*(r+1))-(r*r));
     r=r+2;
     } 
     printf("Case #%d: %d\n",a,count);
     a++;
     }
     return 0;
     }
