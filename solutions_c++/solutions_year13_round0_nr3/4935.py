#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<stdlib.h>
using namespace std;
int T,A,B;
int a[1011];
int f(int x)
{
  int i,j,k;
  k=0;
  j=x;
  while(x!=0)
   {
     a[k]=x%10;
     x/=10;
     k++;
   }
  k--;
 // printf("%d\n",j);
 // for(i=0;i<=k;i++)printf("%d",a[i]);printf("\n");
  
  for(i=0;i<=k;i++)
   {
 //    printf(".%d %d\n",i,k-i);
 //    printf(".%d %d\n",a[i],a[k-i]);
     if(a[i]!=a[k-i])return 0;
   }
  return 1;
}
int main()
{
 freopen("C-small-attempt0.in","r",stdin);
freopen("C-small-attempt0.out","w",stdout);
    int i,j,k;
    int p,q,r;
    int t,tt,ttt;
    double d,dd,ddd;
scanf("%d",&T);
for(int ii=1;ii<=T;ii++)
{
   k=0;
   scanf("%d %d",&A,&B);
   for(i=A;i<=B;i++)
    {
      d=i;
      dd=sqrt(d);
      p=dd;
      dd=p;
      if(dd*dd==d)
       {
         r=0;
         if(f(p)==1)r++;
         if(f(i)==1)r++;
         if(r==2)k++;
       }
    }
   printf("Case #%d: %d",ii,k);
   if(ii<=T-1)printf("\n");
}
    
    
    
    scanf(" ");
    return 0;
}
