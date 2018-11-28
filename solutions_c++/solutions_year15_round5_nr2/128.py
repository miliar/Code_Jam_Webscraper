#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <vector>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

int t;

int n, k;
ll s[1234];
ll up[1234], down[1234];
ll sup, sdown;

ll floor(ll x, ll y)
{
	if(x%y==0) return x/y;
	if((x>0 && y>0) || (x<0 && y<0)) return abs(x)/abs(y);
	return -(abs(x)/abs(y))-1;
}

ll ceil(ll x, ll y)
{
	if(x%y==0) return x/y;
	if((x>0 && y>0) || (x<0 && y<0)) return abs(x)/abs(y)+1;
	return -(abs(x)/abs(y));
}

int main()
{
	scanf("%d", &t);

for(int q=1; q<=t; q++) {
	scanf("%d%d", &n, &k);
	for(int i=0; i<n-k+1; i++) scanf("%lld", &s[i]);
	for(int i=0; i<k; i++) up[i]=down[i]=0;
	for(int i=0; i<k; i++) {
		ll cur=0;
		for(int j=i; j+k<n; j+=k) {
			cur+=s[j+1]-s[j];
			if(cur>0) up[i]=max(up[i], cur);
			if(cur<0) down[i]=max(down[i], -cur);
		}
	}
	sup=sdown=0;
	for(int i=0; i<k; i++) sup+=up[i];
	for(int i=0; i<k; i++) sdown+=down[i];
	ll x=(s[0]-sdown)/k+5;
	while(k*x>s[0]-sdown) x--;
	ll ans=(s[0]+sup-k*x)/k-4;
	while(k*ans<s[0]+sup-k*x) ans++;

	for(int i=0; i<k; i++) ans=max(ans, up[i]+down[i]);

	printf("Case #%d: %lld\n", q, ans);
}

	return 0;
}
