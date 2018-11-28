#include<iostream>
#include<cstdio>
long count[1001][1001];
int dis=100;
int main()
{
   FILE *fp,*fpw;
   long i,j,k,l,n,m,a,b,c;
   m=0;
   for(k=0;k<=1000;k++)
   {
      for(j=0;j<=1000;j++)
      {
         count[k][j]=k&j;
      }
   }
   fp=fopen("input.txt","r");
   fpw=fopen("output.txt","w");
   fscanf(fp,"%ld",&m);
   for(i=1;i<=m;i++)
   {
      fscanf(fp,"%ld%ld%ld",&a,&b,&c);
      n=0;
      for(k=0;k<a;k++) for(j=0;j<b;j++) if(count[k][j]<c) n++;
      fprintf(fpw,"Case #%ld: %ld\n",i,n);
   }
}
