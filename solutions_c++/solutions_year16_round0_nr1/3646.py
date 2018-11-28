#include<bits/stdc++.h>

using namespace std;

#define dbg(x) (cout<<#x<<" = "<<(x)<<'\n')

typedef long long int lld;
const int INF = (1LL << 30) - 1;
const lld LINF = (1LL << 62) - 1;

int N;

lld sol(int N) {
	bitset<10> viz = 0;
	for (int i = 1; i <= 1e6; i++) {
		lld aux = N * 1LL * i;
		while (aux) {
			viz[aux % 10] = 1;
			aux /= 10;
		}
		if (viz.count() == 10)
			return N * 1LL * i;
	}
	return -1;
}

int main() {
	cin.sync_with_stdio(false);

	#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

	int nrtests;

	scanf("%d", &nrtests);

	for (int testcase = 1; testcase <= nrtests; testcase++) {
		scanf("%d", &N);
		lld s = sol(N);
		if (s == -1) printf("Case #%d: INSOMNIA\n", testcase);
		else printf("Case #%d: %lld\n", testcase, s);
	}

	return 0;
}