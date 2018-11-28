#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
using namespace std;
double a[1200],b[1200],ta[1200],tb[1200];
bool xxx(double a,double b) {return a>b;}
int main(void)
{
   int T,TT,sum,i,j,k,a_ans,b_ans,l,r,t,rr;
   FILE *fpi,*fpo;
   fpi=fopen("D-large.in","rt");
   fpo=fopen("zz.out","wt");
   fscanf(fpi,"%d",&TT);
   for(T=0;T<TT;T++)
   {
      
      fscanf(fpi,"%d",&sum);
      for(i=0;i<sum;i++)
         fscanf(fpi,"%lf",&a[i]);
      for(i=0;i<sum;i++)
         fscanf(fpi,"%lf",&b[i]);
      sort(a,a+sum,xxx);
      sort(b,b+sum,xxx);
      for(i=0;i<sum;i++)
      {
         ta[i]=a[i];
         tb[i]=b[i];
      }
      a_ans=b_ans=0;
      l=0;r=sum-1;
      for(i=0;i<sum;i++)
      {
         if(ta[i]>tb[l])
         {
            r--;
            a_ans++;
         }
         else
            
            l++;
      }
      
      for(i=0;i<sum;i++)
      {
         t=0;
         rr=sum-i;
         l=i;
         r=sum-1;
         for(j=0;j<rr;j++)
         {
            if(a[j]>b[j+l])
               t++;
            else
               break;
         }
         if(t>b_ans)
         b_ans=t;
      }
      fprintf(fpo,"Case #%d: %d %d\n",T+1,b_ans,a_ans);
   }
   
}
