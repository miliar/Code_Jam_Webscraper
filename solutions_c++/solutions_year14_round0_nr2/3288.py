#include<iostream>
#include<cstdio>
int main()
{
   FILE *fp,*fpw;
   int i,j,k,l,n,m;
   double ans,c,f,x,cps,min,prev;
   fp=fopen("input.txt","r");
   fpw=fopen("output.txt","w");
   fscanf(fp,"%d",&m);
   for(i=1;i<=m;i++)
   {
      fscanf(fp,"%lf%lf%lf",&c,&f,&x);
      cps=2;
      min=x;
      ans=0;
      for(prev=0;ans<=min;cps+=f)
      {
         ans=prev+x/cps;
         prev+=c/cps;
         if(ans<min) min=ans;
      }
      fprintf(fpw,"Case #%d: %.7lf\n",i,min);
   }
}
