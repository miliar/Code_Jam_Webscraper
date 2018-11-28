#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
int comp(const void *a,const void *b)
{
const long long *p=(long long *)a;
const long long *q=(long long *)b;
return *p-*q;
 
}
void fun(long long i,long long count,long long sum);
 
 
long long a[1000],dp[1000],ans,n;
int main()
{
long long sum,s,i,test,t,count;
 
scanf("%lld",&test);
 
for(t=1;t<=test;t++)
{
scanf("%lld %lld",&s,&n);
 
for(i=0;i<n;i++)
{
scanf("%lld",&a[i]);
dp[i]=-1;
}
qsort(a,n,sizeof(long long),comp);
ans=LONG_MAX;
fun(0,0,s);
printf("Case #%lld: %lld\n",t,ans);
 
}
 
return 0;
 
}
 
void fun(long long i,long long count,long long sum)
{
 
if(i>=n)
{
if(count<ans)
ans=count;
return;
}
 
if(a[i]<sum)
{
dp[i]=count;
fun(i+1,count,sum+a[i]);
}
else
{
if(2*sum-1>sum)
fun(i,count+1,2*sum-1);
fun(i+1,count+1,sum); 
}
}
