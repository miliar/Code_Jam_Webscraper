#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
int main()
{
FILE *ifp,*ofp;
ifp=fopen("A-large.in","r");
ofp=fopen("outputCJ1","w");
int T,smax,i,j,a,p,length;
char str[1005];
//scanf("%d",&T);
fscanf(ifp,"%d",&T);
for(i=0;i<T;i++)
{
p=0;

fscanf(ifp,"%d",&smax);
fscanf(ifp,"%s",str);
fprintf(ofp,"Case #%d: ",(i+1));
length=strlen(str);
//printf("%s",str);
a=0;
for(j=0;j<length;j++)
{
if(str[j]!='0')
{
if(j-p-a>0)
{
a=j-p;
}
p=p+str[j]-'0';

}
}
fprintf(ofp,"%d\n",a);
}
}
