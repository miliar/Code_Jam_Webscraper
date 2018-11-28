#include<iostream>

#include<algorithm>

using namespace std;

int main()

{

int t,n,count,p,i,j,s,k,flag;

double a[10],b[10];

scanf("%d",&t);

for(p=1;p<=t;p++)

{

count=0;
scanf("%d",&n);

for(i=0;i<n;i++)

scanf("%lf ",&a[i]);

for(i=0;i<n;i++)

scanf("%lf ",&b[i]);

sort(a,a+n);

sort(b,b+n);

k=0;

for(i=0;i<n;i++)

{

for(j=k;j<n;j++)
{

if(b[j]>a[i])
{
count++;
j++;
break;
}

}

k=j;

}

k=n-1;

s=0;

for(i=n-1;i>=s;i--)

{

flag=0;
for(j=k;j>=0;j--)
{
if(b[j]>a[i])
s++;
else
{
flag=1;
break;
}
}

if(flag==1)

j=j-1;

k=j;
}

printf("Case #%d: %d %d\n",p,n-s,n-count);
}
return 0;
}