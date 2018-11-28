#include<bits/stdc++.h>
using namespace std;
int main()
{
int t;
scanf("%d",&t);
for(int j=1;j<=t;j++)
{
bool ans=true;
bool A[10];
memset(A,false,sizeof(A));
long long n;
scanf("%lld",&n);
long long i;
for(i=1;n;i++)
{
long long  a=(long long)i*n;
while(a)
{
A[a%10]=true;
a/=10;
}
ans=true;
for(int i=0;i<10;i++)
if(!A[i])
ans=false;
if(ans)
break;
}
if(ans&&n)
printf("Case #%d: %lld\n",j,n*i);
else
printf("Case #%d: INSOMNIA\n",j);
}
return 0;
}
