#include<bits/stdc++.h>
using namespace std;
int main()
{
freopen("in.in","r",stdin);
freopen("out.out","w",stdout);
int t;
cin>>t;
for(int k=1; k<=t; k++)
{
int a[10];
fill(a,a+10,0);
long long int n;
cin>>n;
if(n==0)
    printf("Case #%d: INSOMNIA\n",k);
else
{
long long int d;
int c=0,i=1;
while(c<10)
{
d=n*i;
i++;
while(d!=0)
{
int r=d%10;
if(a[r]==0)
{
a[r]=1;
c++;
}
d=d/10;
}
}
printf("Case #%d: %lld\n",k,(n*i)-n);
}
}
return 0;
}
