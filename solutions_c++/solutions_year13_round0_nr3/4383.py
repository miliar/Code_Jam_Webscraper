// C - Fair and Square
// wahyuoi

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <cmath>
using namespace std;
#define ll long long
#define INF 1000000000
#define debug puts("DEBUUGG")
#define vi vector<ll>
#define pii pair<ll,ll>
#define vii vector<pii>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define rep(a,b,c) for(a=b;a<c;a++)
#define repe(a,b,c) for(a=b;a<=c;a++)
#define repd(a,b,c) for(a=b-1;a>=c;a--)
#define ALL(a) a.begin(),a.end()
#define MAX_B 100000000000010 // small input
#define MAX_A 10000009
ll data[MAX_A];
bool cek(ll s){
	ll v = s;
	ll n=0;
	ll x=1;
	while(v){
		n = n*10+(v%10);
		v/=10;
		x*=10;
	}
	v=n;
	while(s)
	{
		if (s%10!=v%10)
		{
			return false;
		}
		s/=10;
		v/=10;
	}
	return true;
}
void generate(){
	ll sq = MAX_A;
	data[0]=0;
	for (ll i=1;i<=sq ;++i )
	{
		if (cek(i))
		{
			if (cek((i*i)))
			{
				data[i]=data[i-1]+1;
			} else data[i]=data[i-1];
		} else data[i]=data[i-1];
	}

}
void solve(ll tc){
	ll x,y;
	scanf("%lld %lld",&x,&y);
	ll xx = (int) sqrt(x);
	ll yy = (int) sqrt(y);
	if (xx*xx<x)
	{
		++xx;
	}
	if (yy*yy>y)
	{
		--yy;
	}
	printf("Case #%lld: %lld\n",tc,data[yy]-data[xx-1]);
	fprintf(stderr,"Case #%lld: %lld\n",tc,data[yy]-data[xx-1]);
}
int main(){
	ll nn;
	scanf("%lld",&nn);
	generate();
	for (ll tc=1;tc<=nn ;++tc )
	{
		solve(tc);
	}
}
