#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
int main()
{
int t,m=1;
scanf("%d",&t);
while(t--)
{
int n,i,c=0,l=0,pos=0,j=0,k=0;
scanf("%d",&n);
double ar[n],br[n],a[n],b[n];

for(i=0;i<n;i++)
{
scanf("%lf",&ar[i]);
}

for(i=0;i<n;i++)
{
scanf("%lf",&br[i]);
}
std::sort(ar,ar+n);
std::sort(br,br+n);

for(i=0;i<n;i++)
{
a[n-1-i]=ar[i];
b[n-1-i]=br[i];
}

for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if(br[j])
{
if(br[j]>ar[i])
{
br[j]=0;
c++;
break;
}
}
}
}
c=n-c;

k=0;
l=0;

for(i=0;i<n;i++)
printf("%lf ",b[i]);

for(i=0;i<n;i++)
{

A:
for(j=n-1;j>=0;j--)
{
if(b[j])
{
if(ar[i]>b[j])
{
l++;
b[j]=0;
ar[i]=0;
goto A;
}
else
{
 b[k++]=0;
 ar[i]=0;
 goto A;
 }
}

}
}


printf("Case #%d: %d %d\n", m++,l,c);
}
return 0;
}
