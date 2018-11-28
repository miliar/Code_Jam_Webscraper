#include <cstdio>
#include <cstring>

using namespace std;

int main() {
	freopen("pank.in", "r", stdin);
	freopen("pank.out", "w", stdout);

	int t;
	scanf("%d\n", &t);

	char str[101];

	for (int i = 1; i <= t; ++i) {
		memset(str, 0, sizeof(str));
		fgets(str, sizeof(str), stdin);

		int n = strlen(str) - 1;
		int losh = 1; // length of compacted string

		for (int j = 1; j < n; ++j) {
			if (str[j] != str[j-1]) {
				++losh;
			}
		}

		if (str[n-1] == '+')
			--losh;

		printf("Case #%d: %d\n", i, losh);
	}

	return 0;
}

