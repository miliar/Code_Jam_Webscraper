#include<algorithm>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int T;
int a[20];
int main()
{
freopen("A-small-attempt0.in","r",stdin);
freopen("A-small-attempt0.out","w",stdout);    
    int i,j,k;
    int p,q,r;
    int t,tt,ttt;
    scanf("%d",&T);
for(int ii=1;ii<=T;ii++)
  {
     scanf("%d",&t);
     for(i=0;i<19;i++)a[i]=0;
     for(i=1;i<=4;i++)
      {
        for(j=1;j<=4;j++)
         {
           scanf("%d",&k);
           if(i==t)a[k]++;
         }
         
      }
     scanf("%d",&t);
     for(i=1;i<=4;i++)
      {
        for(j=1;j<=4;j++)
         {
           scanf("%d",&k);
           if(i==t)a[k]++;
         }
      }
     p=0;
     for(i=0;i<19;i++)
      {
        if(a[i]==2)p++;
      }
     printf("Case #%d: ",ii);
     if(p==0)printf("Volunteer cheated!");
     else if(p==1)
      {
        for(i=0;i<19;i++)
         {
           if(a[i]==2)printf("%d",i);
         }
      }
     else printf("Bad magician!");
     if(ii<=T-1)printf("\n");
  }
     
    
    scanf(" ");
    return 0;
}
