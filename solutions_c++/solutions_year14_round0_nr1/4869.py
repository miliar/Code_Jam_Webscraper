#include <stdlib.h>
#include <stdio.h>
int main(void)
{
   int T,x[4],i,j,a,sum,ans,k,zzz,zxcc;
   FILE *fpi,*fpo;
   fpi=fopen("A-small-attempt0.in","rt");
   fpo=fopen("zz.out","wt");
   fscanf(fpi,"%d",&T);
   for(zzz=0;zzz<T;zzz++)
   {
      ans=0;
      fscanf(fpi,"%d",&sum);
      for(i=1;i<=4;i++)
      {
         if(i==sum)
            for(j=0;j<4;j++)
               fscanf(fpi,"%d",&x[j]);
         else
            for(j=0;j<4;j++)
               fscanf(fpi,"%d",&a);
      }
      fscanf(fpi,"%d",&sum);
      for(i=1;i<=4;i++)
      {
         if(i==sum)
         {
            for(j=0;j<4;j++)
            {
               fscanf(fpi,"%d",&a);
               for(k=0;k<4;k++)
               {
                  if(a==x[k])
                  {
                     zxcc=a;
                     ans++;
                  }
               }
            }
         }
         else
            for(j=0;j<4;j++)
               fscanf(fpi,"%d",&a);
      }
      if(ans==0)
         fprintf(fpo,"Case #%d: Volunteer cheated!\n",zzz+1);
      else if(ans==1)
         fprintf(fpo,"Case #%d: %d\n",zzz+1,zxcc);
      else
         fprintf(fpo,"Case #%d: Bad magician!\n",zzz+1);
      
   }
}
