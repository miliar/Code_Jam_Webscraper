#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;
int main()
{
    freopen("Magic Trick.out","w",stdout);
    freopen("magic.in","r",stdin);
    int t[2][4];
    int i,j;
    int a,b;
    int r,ok,rr=1;
    cin>>r;
    while(r--)
    {
       cin>>a;
       for(i=0;i<4;i++)
         for(j=0;j<4;j++)
           if(i==a-1) cin>>t[0][j];
           else cin>>b;
       cin>>a;
       for(i=0;i<4;i++)
         for(j=0;j<4;j++)
           if(i==a-1) cin>>t[1][j];
           else cin>>b;
       ok=0;
       for(i=0;i<4;i++)
         for(j=0;j<4;j++)
         if(t[0][i]==t[1][j]) { b=t[0][i]; ok++;}
       printf("Case #%d:",rr++);
       if(ok==0) printf(" Volunteer cheated!\n");
       if(ok==1) printf(" %d\n",b);
       if(ok>=2) printf(" Bad magician!\n");
    }
    return 0;
}
