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
//q=0;

while(t--)
{
	ll cnt=0;
q++;
ll n1;
n1=readLong();
if(n1==0)
{
	printf("Case #1: INSOMNIA\n");
	continue;
}
//for(n1=1;n1<=200;n1++){
	
//q++;
ll n2;
n2=n1;
int f1=0;
int fr[10]={0};
ll q1=1;
ll n3;
while(1)
{
	n2=q1*n1;
	n3=n2;
	q1++;
while(n2)
{
	fr[n2%10]++;
	int f=0;
	for(i=0;i<=9;i++)
	{
		if(fr[i]>=1)
		f++;
	}
	if(f==10)
	{
		f1=1;
		break;
	}
	n2/=10;
}
if(f1==1)
break;
}

	printf("Case #%d: %lld\n",q,n3);
}
//}
return 0;
}