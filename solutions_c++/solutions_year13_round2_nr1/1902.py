#include<algorithm>
#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
long long int h,p,fl,an=0,cn=0,s=0,t,n,a,arr[101],i,j,k;
scanf("%lld",&t);
while(t--)
{
an=0;fl=1,h=0,p=0;
k=100000000000;
scanf("%lld%lld",&s,&n);
for(i=0;i<n;i++)
scanf("%lld",&arr[i]);
sort(arr,arr+n);

for(i=0;i<n;i++)
{
if(arr[i]<s)
s=s+arr[i];
else
{
//printf("%lld\n",s);
p=1;
if(fl)
{
k=min(k,an+n-i);
fl=0;
}
if(s!=1)
{
//printf("y");
while(s<=arr[i])
{
s+=(s-1);
an++;
fl=1;
h=1;
}
s+=arr[i];
}
else
an++;
//printf("%lld %lld\n",an,s);
}
}
cn++;
//printf("%lld %lld\n",k,an);
if(h)
k=min(k,an);
if(p==0)
k=0;
printf("Case #%lld: %lld\n",cn,k);
}
return(0);
}
