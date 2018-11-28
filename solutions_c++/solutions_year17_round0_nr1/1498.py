#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
typedef long long i64;

int T;
char S[1010]; int K;

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T; ) {
		scanf("%s%d", S, &K);
		printf("Case #%d: ", t);

		int N = strlen(S);
		int ans = 0;
		for (int i = 0; i <= N - K; ++i) {
			if (S[i] == '-') {
				++ans;
				for (int j = 0; j < K; ++j) {
					S[i + j] = (S[i + j] == '+' ? '-' : '+');
				}
			}
		}
		for (int i = 0; i < N; ++i) {
			if (S[i] != '+') ans = -1;
		}

		if (ans == -1) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}
