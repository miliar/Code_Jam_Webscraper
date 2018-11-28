#pragma comment(linker, "/STACK:65000000")
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<complex>
#include<ctime>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vi;
typedef vi::iterator vit;
typedef vector<pii> vpi;

#define sq(x) (x)*(x)
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
#define LL "%I64d"
#define RLL(x) scanf(LL,&(x))

ll mas[105][105];
ll mn[2][105];
ll mx[2][105];

void test(ll t)
{
	cl(mn);
	cl(mx);
	ll n,m;
	RLL(n);
	RLL(m);
	for(ll i=0; i<105; ++i)
		mn[0][i]=mn[1][i]=1000;
	for(ll i=0; i<n; ++i)
		for(int j=0; j<m; ++j)
		{
			RLL(mas[i][j]);
			mn[0][i] = min(mn[0][i],mas[i][j]);
			mn[1][j] = min(mn[1][j],mas[i][j]);
			mx[0][i] = max(mx[0][i],mas[i][j]);
			mx[1][j] = max(mx[1][j],mas[i][j]);
		}
	bool b=true;
	for(ll i=0; i<n; ++i)
		for(ll j=0; j<m; ++j)
			if(mas[i][j]<mx[0][i] && mas[i][j]<mx[1][j])
				b=false;
	if(b)
		printf("Case #%I64d: YES\n",t);
	else
		printf("Case #%I64d: NO\n",t);
}

int main()
{
	freopen("b.in","r",stdin);freopen("b.out","w",stdout);
	ll n;
	cin>>n;
	for(ll i=1; i<=n; ++i)
		test(i);
	return 0;
}