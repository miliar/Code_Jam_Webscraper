#include "stdio.h"
#include<conio.h>
#include<iostream>
#include<stdlib.h>
void main()
{
FILE *fp,*f;
int i,j=1,k,p[10],nt;
long int a,n,t;
fp=fopen("code.txt","r");
f=fopen("code1.txt","w");
//freopen("C:\Users\user\Downloads\A-small-attempt2.in","r",stdin);
//freopen("C:\Users\user\Downloads\a.out","w",stdout);
fscanf(fp,"%d",&nt);
//printf("%ld",nt);

for(i=0;i<nt;i++)
{
  fscanf(fp,"%ld",&a);
  k=10;
  j=1;
  if(a!=0)
  while(1)
  {
     n=a*j++;
     t=n;
     while(n)
     {
         if(p[n%10]!=i)
         {
         p[n%10]=i;
         k--;
         }
         n=n/10;    
     }
     if(k==0)
     {
     fprintf(f,"Case #%d: %ld\n",i+1,t);
     break;
     }   
  }
  else
    fprintf(f,"Case #%d: INSOMNIA\n",i+1);
}
fcloseall();	


}