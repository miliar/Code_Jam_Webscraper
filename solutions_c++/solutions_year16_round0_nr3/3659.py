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
    temp=p(a,b/2);
    if(b&1)
    return (((a*temp))*temp);
    else
    return (temp*temp);
}


 
 int i,j,k,n,m,q;
 
 int check(ll a)
 {
 	ll i1;
 	int f=0;
 	for(i1=2;i1<=sqrt(a);i1++)
 	{
 		if(a%i1==0)
 		{
 			f=1;
 			break;
 		}
 	}
 	if(f==0)
 	return 0;
 	return i1;
 }



int main() {

	int t,h;
t=readInt();
q=0;

while(t--)
{
	int cnt=0;
	q++;
	printf("Case #%d:\n",q);
n=readInt();
int ar[n+1];
ll ar1[20];
m=readInt();
int num=p(2,n);
int size=n;
for(i=0;i<=num;i++)
{
	int f=0;
	size=n;
h=0;
	for(k=2;k<=10;k++)
	{
	
		ll nu=0;
		if(i&(p(2,0)) && i&(p(2,n-1)))
		{
	for(j=0;j<n;j++)
	{
			if(i&p(2,j))
			{
				
			ar[--size]=1;
			nu+=p((ll)k,(ll)j);
			}
			else ar[--size]=0;
	}
	
		}
		ll v=check(nu);
		if(v==0)
		{
			f=1;
			break;
		}
		else
		{
			ar1[h++]=v;
		}
	}
	if(f==0)
	{
		cnt++;
		for(j=0;j<n;j++)
		{
			printf("%d",ar[j]);
		}
		printf(" ");
		for(j=0;j<h;j++)
		cout<<ar1[j]<<" ";
		printf("\n");
		if(cnt==m)
		{
			break;
		}
	}
}
}
return 0;
}