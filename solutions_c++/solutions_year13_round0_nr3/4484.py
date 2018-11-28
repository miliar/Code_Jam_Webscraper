#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
using namespace std;
#define maxn 107
int tem[maxn]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002,10000001,10011001,10100101,10111101,11000011,11011011,11100111,11111111};
int n,m;
int ha(int a,int b)
{
   int tem1=sqrt(a-1);
   int tem2=sqrt(b);
   int i=0,j=0;
   if(a!=1)
   for(i=0;i<47;i++)
   {
       if(tem1<tem[i]) break;
   }
   for(j=0;j<47;j++)
   {

       if(tem2<tem[j]) break;
   }
   return j-i;
}
int main()
{
    //freopen("C-small-attempt2.in","r",stdin);
   // freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    int t;
    int cnt=0;
    scanf("%d",&t);
    while(t!=cnt)
    {
        cnt++;
        int ans=0;
        scanf("%d%d",&n,&m);
        ans=ha(n,m);
        printf("Case #%d: %d\n",cnt,ans);
    }
    return 0;
}
