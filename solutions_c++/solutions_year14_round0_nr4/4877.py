


#include<bits/stdc++.h>
#include<stdlib.h>
using namespace std;
int main()
{
int t,pp=0;
scanf("%d",&t);
while(t--)
{
pp++;
int n,i,j,c=0;
scanf("%d",&n);
long double a[n+1],b[n+1],aa[n+1],bb[n+1];
for(i=0;i<n;i++)
{
scanf("%Lf",&a[i]);
aa[i]=a[i];
}
for(i=0;i<n;i++)
{
scanf("%Lf",&b[i]);
bb[i]=b[i];
}
std::sort(a,a+n);
std::sort(b,b+n);
std::sort(aa,aa+n);
std::sort(bb,bb+n);
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if(((double)bb[j]>(double)aa[i]) && ((double)aa[i]!=0.0) &&((double)bb[j]!=0.0))
{
bb[j]=0.0;
aa[i]=0.0;
c++;
break;
}
}
}

//std::reverse(a,a+n);
std::reverse(b,b+n);

/*for(i=0;i<n;i++)
printf("%f ",a[i]);
printf("\n");
for(i=0;i<n;i++)
printf("%f ",b[i]);*/
float temp1,temp2=1000.0;
int pos,cc=0,k=n-1;


for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if(a[i]>b[k] &&a[i]!=0 &&b[k]!=0)
{
a[i]=0;
b[k]=0;
k--;
cc++;
}
else if(a[i]<b[j] && a[i]!=0 && b[j]!=0)
{
a[i]=0;
b[j]=0;
}
}
}

printf("Case #%d: %d ",pp,cc);

if(c==n)
printf("0\n");
else
printf("%d\n",n-c);




}
return 0;
}
