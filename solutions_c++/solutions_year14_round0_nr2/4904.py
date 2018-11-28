#include <stdlib.h>
#include <stdio.h>
int main(void)
{
   int zzz,i,j,T;
   double c,f,x,ans=1000000,t,sp,k;
   FILE *fpi,*fpo;
   fpi=fopen("B-small-attempt0.in","rt");
   fpo=fopen("zz.out","wt");
   fscanf(fpi,"%d",&T);
   for(zzz=0;zzz<T;zzz++)
   {
      ans=1000005;
      fscanf(fpi,"%lf %lf %lf",&c,&f,&x);
      ans=x/2;
      for(i=1;i<10000;i++)
      {
         t=0;
         sp=2;
         for(k=0;k<i;k++)
         {
            t+=c/sp;
            sp+=f;
         }
         t+=x/sp;
         if(t<ans)
            ans=t;
         else
            break;
      }
      fprintf(fpo,"Case #%d: %.7lf\n",zzz+1,ans);
   }
}
