#include <cstdio>
#include <cstdlib>

using namespace std;

const int S_MAX = 1001;
int S[S_MAX];


int main() {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		char c;
		int n, j = 0;
		scanf("%d", &n);
		getchar();
		while ((c = getchar()) != '\n') {
			S[j++] = (int) c - '0';
		}
		int result = 0;
		int klaszcze = S[0];
		for (j = 1; j <= n; ++j) {
			if (S[j] == 0) continue;
			if (klaszcze < j) {
				result += j - klaszcze;
				klaszcze = j;
			}
			klaszcze += S[j];
		}
		printf("Case #%d: %d\n", i + 1, result);
	}
	return 0;
}