#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
 int t,k;
 double c,f,x;
 freopen("B-large.in","r",stdin);
 freopen("gcj2.txt","w",stdout);
 scanf("%d",&t);
 for(k=1;k<=t;k++)
 {
  scanf("%lf %lf %lf",&c,&f,&x);
  double time=0,nc=0,r=2;
  while(1)
  {
   double tr=x/r,er=c/r+x/(r+f),min;
   if(tr<=er)
   {
    time+=tr;break;          
   }
   else
   {
    time+=c/r;r+=f;    
   }           
  }
  printf("Case #%d: %.7lf\n",k,time);         
 }   
 return 0;    
}
