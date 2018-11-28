#include<bits/stdc++.h>
#include<ext/numeric>
using namespace std;
using namespace __gnu_cxx;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v)  (int)v.size()
#define UNVISITED -1
#define CLR(a,v) memset(a,v,sizeof a)
#define PC(x) __builtin_popcount(x)

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;
typedef unsigned long long ull;

int dx[] = { 0, 0, 1, -1, -1, -1, 1, 1 };
int dy[] = { 1, -1, 0, 0, 1, -1, 1, -1 };

bool frq[10];
int cnt;
void countNum(ll n) {
	while (n) {
		int x = n % 10;
		if (!frq[x])
			frq[x] = 1, ++cnt;
		n /= 10;
	}
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int c = 1; c <= t; ++c) {
		CLR(frq, 0);
		cnt = 0;
		printf("Case #%d: ", c);
		ll n;
		scanf("%lld", &n);
		if (!n) {
			puts("INSOMNIA");
			continue;
		}
		ll step = n;
		while (1) {
			countNum(n);
			if (cnt == 10) {
				printf("%lld\n", n);
				break;
			}
			n += step;
		}
	}
}

