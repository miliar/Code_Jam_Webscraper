#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <sstream>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

#define ll long long
#define PII pair<int,int>
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define SIZE(v) (int)v.size()

int T,cs,N;
ll P;

int go1(int n, ll u) {
	if(u == 0) return 1;
	ll wins = (u - 1) / 2;
	return (1ll<<(n-1)) + go1(n - 1, wins);
}

int go2(int n, ll u) {
	if(u == 0) return 1;
	if(u == (1ll<<n)-1) return u + 1;
	ll wins = (u + 1) / 2;
	return go2(n - 1, wins);

}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d",&T);
	for(cs=1;cs<=T;++cs) {
		scanf("%d%lld",&N,&P);
		
		ll s = 0, e = (1ll<<N) - 1, ans1 = -1, ans2 = -1;
		while(s <= e) {
			ll m = (s + e ) / 2;
			if(go1(N,m) <= P) ans1 = m, s = m + 1;
			else e = m - 1;
		}
		s = 0, e = (1ll<<N) - 1;
		while(s <= e) {
			ll m = (s + e ) / 2;
			if(go2(N,m) <= P) ans2 = m, s = m + 1;
			else e = m - 1;
		} printf("Case #%d: %lld %lld\n",cs,ans1,ans2);
	}
}