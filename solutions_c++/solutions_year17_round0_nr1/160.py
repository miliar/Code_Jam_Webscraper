#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sz(x) ((int)(x).size())
#define rep(i,l,r) for(int i=(l);i<(r);++i)
//-------
const int N = 1007;
int k;
char s[N];
bitset<N> S, K;
int solve() {
	S.reset(), K.reset();
	int L = strlen(s);
	rep(i, 0, L)
		if (s[i] == '+')
			S[i] = 1;
//	cout << S << endl;	
	rep(i, 0, k)
		K[i] = 1;
	int ret = 0;
	rep(i, 0, L - k + 1) {
		if (S[i] == 0)
			S ^= K, ++ret;
		K <<= 1;
	}
//	printf("ret = %d\n", ret);
	rep(i, L - k + 1, L)
		if (S[i] == 0)
			return -1;
	return ret;
}
int main() {
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	rep(cas, 0, T) {
		scanf(" %s %d", s, &k);
		printf("Case #%d: ", cas + 1);
		int ans = solve();
		if (~ans) {
			printf("%d\n", ans);
		} else {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}
