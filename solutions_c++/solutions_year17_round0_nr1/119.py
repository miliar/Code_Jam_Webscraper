#include <cstdio>
#include <cstring>

const int MAX = 1020;

char cake[MAX];
int flipSize;

void solve() {
	int ans = 0;

	int len = strlen(cake);
	for (int i = 0; i <= len-flipSize; i++) {
		if (cake[i] == '-') {
			ans++;
			for (int j = i; j < i+flipSize; j++) {
				cake[j] = cake[j] == '+' ? '-' : '+';
			}
		}
	}

	// final check
	for (int i = len-flipSize+1; i < len; i++) {
		if (cake[i] == '-') {
			puts("IMPOSSIBLE");
			return;
		}
	}

	printf("%d\n", ans);
}

int main() {
	freopen("output.txt", "w", stdout);

	int numCase;
	scanf("%d", &numCase);
	for (int nowCase = 1; nowCase <= numCase; nowCase++) {
		scanf("%s%d", cake, &flipSize);

		printf("Case #%d: ", nowCase);
		solve();
	}

	return 0;
}