#include <bits/stdc++.h>

using namespace std;

#define st first
#define nd second
#define mp make_pair
#define pb push_back

void openFile() {
	freopen("in.inp", "r", stdin);
	freopen("ou.out", "w", stdout);
}

int main(int argc, char **argv) {
	openFile();
	int T, K, S, C;
	scanf("%d", &T);
	for (int itest = 0; itest < T; ++itest) {
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d: ", itest + 1);
		long long ans;
		for (int i = 1; i <= K; ++i) {
			ans = i;
			for (int j = 1; j < C; ++j)
				ans = (ans - 1) * K + i;
			printf("%lld ", ans);
		}
		printf("\n");
	}

	return 0;
}
