#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
using namespace std;
long long int SQRT[]={0,1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,
     11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,
     1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,
     2001002,10000001};
long long int pal[55];
int main()
{
    int i,j,k,T,c=0,end,st,cnt;
    long long y;
    long long U,L;
    //freopen("C-large-1.in","r",stdin);
    //freopen("outC.out","w",stdout);
    for(i=0; i<=40; i++)
    {
       y=SQRT[i]*SQRT[i];
       pal[i]=y;     
    } 
    scanf("%d",&T);
    while(T--)
    {
       cin>>L>>U;
       cnt=0;
       for(i=0; i<=40; i++)
       {
          if(pal[i]>=L && pal[i]<=U) cnt++;      
       }
       printf("Case #%d: %d\n",++c,cnt);       
    }
    return 0;
}
