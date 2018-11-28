#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
FILE *fin = fopen("B-large.in","r");
FILE *fout = fopen("outputoo.out","w");
int t,i,j,k,flag = 0;
double c,f,x,re,sum = 0,ra = 2.0000000,g = 0;
fscanf(fin,"%d",&t);


for(i=0;i<t;i++)
{
fscanf(fin,"%lf%lf%lf",&c,&f,&x);
flag = 0;
g = 0;
ra = 2.0000000;
while(flag == 0)
{
sum = (c/ra);
re = (x/(ra+f));

if(sum+re < (x/ra)) 
{
g+=sum; ra+=f;
}
else
{
g+=(x/ra);
flag = 1;
}

}

fprintf(fout,"Case #%d: %0.7lf\n",i+1,g);
}
return 0;
}
