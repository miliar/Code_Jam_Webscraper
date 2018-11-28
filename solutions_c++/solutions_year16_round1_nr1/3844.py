

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
int h;
char str[100001];
char str1[100001];
char str2[100001];
int main() {
    //freopen("cj1i1.txt", "r", stdin);
//freopen("cj1o1.txt", "w", stdout);
	int t;
t=readInt();
q=0;
while(t--)
{
	h=10000;
	q++;
scanf("%s",str);
str1[h]=str[0];
int st=h;
for(i=1;str[i];i++)
{
	if(str[i]>=str1[st])
	{
		st--;
		str1[st]=str[i];
	}
	else
	{
		h++;
		str1[h]=str[i];
	}
}
int w=0;
for(i=st;i<=h;i++)
str2[w++]=str1[i];
str2[w]='\0';
printf("Case #%d: %s\n",q,str2);
}
return 0;
}
