#include<iostream>
#include<cstdio>
#include <algorithm>
using namespace std;
int main()
{
   FILE *fp,*fpw;
   int i,j,k,l,n,m,x,y,a,b;
   double noim[1000],ken[1000];
   fp=fopen("input.txt","r");
   fpw=fopen("output.txt","w");
   fscanf(fp,"%d",&m);
   for(i=1;i<=m;i++)
   {
      fscanf(fp,"%d",&n);
      for(j=0;j<n;j++) fscanf(fp,"%lf",&noim[j]);
      for(j=0;j<n;j++) fscanf(fp,"%lf",&ken[j]);
      sort(noim,noim+n);
      sort(ken,ken+n);
      x=0;
      y=0;
      a=0;
      b=n-1;
      for(j=n-1;j>=0;j--)
      {
         if(noim[b]>ken[j]) b--,y++;
      }
      k=0;
      for(j=0;j<n&&k<n;j++)
      {
         for(;k<n;k++)
         {
            if(noim[j]<ken[k])
            {
               x++;
               k++;
               break;
            }
         }
      }
      x=n-x;
      fprintf(fpw,"Case #%d: %d %d\n",i,y,x);
   }
}
