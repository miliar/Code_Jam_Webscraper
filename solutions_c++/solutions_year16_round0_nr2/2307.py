#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
ll t,n,z,m,k;
scanf("%lld",&z);
for(ll t=1;t<=z;t++)
{
char s[105];

scanf("%s",s);
ll n=strlen(s),cnt=0;

for(int i=1;i<n;i++)
{
if(s[i]!=s[i-1])
{
cnt++;
}
}

if(s[n-1]=='-')
cnt++;


printf("Case #%lld: %lld\n",t,cnt);
}

return 0;
}

