#define _CRT_SECURE_NO_DEPRECATE

#include <set>
#include <stdio.h>

using namespace std;

int T, N;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d", &N);

		if (N == 0) {
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}

		set<int> st;
		bool done = false;
		for (int i = 1; !done; i++) {
			int x = i * N;
			while (x > 0) {
				int d = x % 10;
				x /= 10;

				st.insert(d);
				if (st.size() == 10) {
					printf("Case #%d: %d\n", t, i * N);
					done = true;
					break;
				}
			}
		}
	}

	return 0;
}