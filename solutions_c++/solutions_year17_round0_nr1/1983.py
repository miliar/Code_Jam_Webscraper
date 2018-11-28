#include <cstring>
#include <iostream>
using namespace std;
const int nmax = 1000 + 18;

int T;
char a[nmax];
int S[nmax];
int K, n;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		scanf("%s", a + 1);
		n = strlen(a + 1);
		for (int i = 1; i <= n; ++i) {
			S[i] = a[i] == '+';
		}
		scanf("%d", &K);
		int valid = 1, answer = 0;
		for (int i = 1; i + K - 1 <= n; ++i) {
			if (S[i] != 1) {
				//printf("flip %d\n", i);
				answer += 1;
				for (int j = 0; j < K; ++j)
					S[i + j] ^= 1;
			}
		}
		for (int i = 0; n - i >= 1 && i < K; ++i)
			if (S[n - i] != 1) {
				valid = 0;
				break;
			}
		printf("Case #%d: ", cases);
		if (valid) 
			printf("%d\n", answer);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
