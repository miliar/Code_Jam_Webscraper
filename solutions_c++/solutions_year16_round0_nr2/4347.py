#define ll long long
#define gcd __gcd
#include<bits/stdc++.h>
#define fi first
#define se second
#define mod 1000000007
#define pb push_back
#define N 1000001
using namespace std;
 
int readInt () {
	bool minus = false;
	int result = 0;
	char ch;
	ch = getchar();
	while (true) {
		if (ch == '-') break;
		if (ch >= '0' && ch <= '9') break;
		ch = getchar();
	}
	if (ch == '-') minus = true; else result = ch-'0';
	while (true) {
		ch = getchar();
		if (ch < '0' || ch > '9') break;
		result = result*10 + (ch - '0');
	}
	if (minus)
		return -result;
	else
		return result;
}
 
ll readLong () {
	bool minus = false;
	ll result = 0;
	char ch;
	ch = getchar();
	while (true) {
		if (ch == '-') break;
		if (ch >= '0' && ch <= '9') break;
		ch = getchar();
	}
	if (ch == '-') minus = true; else result = ch-'0';
	while (true) {
		ch = getchar();
		if (ch < '0' || ch > '9') break;
		result = result*10 + (ch - '0');
	}
	if (minus)
		return -result;
	else
		return result;
}
 
ll p(ll a,ll b)
{
    ll temp;
    if(b==0)
    return 1;
    temp=p(a,b/2)%mod;
    if(b&1)
    return (((a*temp)%mod)*temp)%mod;
    else
    return (temp*temp)%mod;
}


 
 int i,j,k,n,m,q;
 
 
char str[101];
int main() {
	int t;
t=readInt();
q=0;
while(t--)
{
	q++;
scanf("%s",str);
int l=strlen(str);
i=0;
ll cnt=0;
while(1)
{
i=0;
while(i+1<l && str[i]==str[i+1])
{
i++;
}
if(i==l-1)
{
if(str[0]=='+')
{
break;
}
else 
{
	cnt++;
	break;
}
}
else
{
	cnt++;
	if(str[0]=='-')
	{
for(j=0;j<=i;j++)
{
str[j]='+';
}
}
else
{
for(j=0;j<=i;j++)
{
str[j]='-';
}	
}
}

}
printf("Case #%d: %lld\n",q,cnt);
}
return 0;
}