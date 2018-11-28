#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cmath>
#include <algorithm>
#include <assert.h>
#include <memory.h>
#include <string.h>
#include <complex>

using namespace std;

#pragma comment(linker, "/STACK:100000000")

#define ll long long
#define pb push_back
#define mp make_pair
#define sz(x) (int)(x).size()
#define fr(i,a,b) for(int i = (a);i <= (b);i++)
#define fd(i,a,b) for(int i = (a);i >= (b);i--)

int ri(){int x;scanf("%d",&x);return x;}

bool vis[10];

bool check(ll N) {
	if(N % 10 == 0) vis[0] = true;
	while(N > 0) {
		vis[N % 10] = true;
		N /= 10;
	}
	for(int i = 0; i < 10; i++) if(!vis[i]) return false;
	return true;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T;
	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		ll N;
		scanf("%lld", &N);
		memset(vis, 0, sizeof(vis));
		int res = 0;
		ll val = N;
		while(!check(val) && res < 10000000) res++, val += N;
		printf("Case #%d: ", i + 1);
		if(check(val)) printf("%lld\n", val);
		else printf("INSOMNIA\n");
	}


	return 0;
}
