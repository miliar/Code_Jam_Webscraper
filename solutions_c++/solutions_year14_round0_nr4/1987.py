#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
freopen("D-large.in","r",stdin);
 freopen("output1.txt","w",stdout);

int t,n,i,l,f1,f2;
float a[1000],b[1000];
scanf("%d",&t);
for(l=1;l<=t;l++)
{
scanf("%d",&n);
for(i=0;i<n;i++)
scanf("%f",&a[i]);
for(i=0;i<n;i++)
scanf("%f",&b[i]);
sort(a,a+n);
sort(b,b+n);
f1=0;
f2=0;
for(i=0;i<n;i++)
{
if(a[i]>b[f1])
{
f1++;
}
if(b[i]>a[f2])
{
f2++;
}
}
printf("Case #%d: %d %d\n",l,f1,(n-f2));
}
return(0);
}

