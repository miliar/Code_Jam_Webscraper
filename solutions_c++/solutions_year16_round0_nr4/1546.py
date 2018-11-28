#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

int solve(int K, int C, int S, ll *ans) {
	int n = K;
	ll s = 0;
	for (int i = 1; i < C; i++) {
		if (n > 1) {
			n--;
			s = (s * K) + i;
		} else {
			s = s * K;
		}
	}
	if (n <= S) {
		for (int j = 0; j < n; j++) {
			ans[j] = s+1+j;
		}
		return n;
	} else {
		return 0;
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int K, C, S;
		scanf("%d%d%d", &K, &C, &S);
		ll ans[110];
		int n = solve(K, C, S, ans);
		printf("Case #%d:", i+1);
		if (n == 0)
			printf(" IMPOSSIBLE\n");
		else {
			for (int j = 0; j < n; j++) {
				printf(" %lld", ans[j]);
			}
			printf("\n");
		}
	}
	
}
