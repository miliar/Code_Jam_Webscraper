#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int K, C, S;

void read() {
	scanf("%d%d%d", &K, &C, &S);
}

void process() {
	if (S * C < K) {
		printf("IMPOSSIBLE\n");
	} else {
		int needed = (K + C - 1) / C;

		int next_to_cover = 1;
		
		for (int i = 1; i <= needed; i++) {

			long long left = 0;
			for (int j = 1; j <= C; j++) {
				left = left * K + (next_to_cover - 1);
				if (next_to_cover < K) {
					next_to_cover++;
				}
			}
			printf(" %lld", left + 1);
		}

		printf("\n");
	}
}

int main() {
	int cases;
	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	return 0;
}