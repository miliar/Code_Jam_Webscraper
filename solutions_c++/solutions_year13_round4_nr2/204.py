#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define rep(i,n) for (int i=0;i<n;i++)
#define ll long long
int T,Case; ll n,p,l,r,m;
bool check1(ll m)
{
	ll x=m;
	for (int i=n-1;i>=0;i--){
		if (p>>i&1) x=(x-1)/2;
		else if (x) return 0;
		if (!x) return 1;
		}
	return 0;
}
bool check2(ll m)
{
	ll y=(1LL<<n)-m-1;
	for (int i=n-1;i>=0;i--){
		if (p>>i&1) {if (y) return 1;}
		else {if (!y) return 0; y=(y-1)/2;}
		}
	return 1;
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	while (T--){
		printf("Case #%d: ",++Case);
		scanf("%lld%lld",&n,&p),p--;
		l=0,r=(1LL<<n)-1;
		while (l<r) m=(l+r+1)/2,check1(m)?l=m:r=m-1;
		printf("%lld ",l);
		l=0,r=(1LL<<n)-1;
		while (l<r) m=(l+r+1)/2,check2(m)?l=m:r=m-1;
		printf("%lld\n",l);
		}
	return 0;
}
