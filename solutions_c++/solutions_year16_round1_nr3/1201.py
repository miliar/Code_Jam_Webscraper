#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;
typedef long long ll;

const int N = 12;
int F[N], perm[N];
bool sat[N];
int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	int _, cas = 1;
	scanf("%d", &_);
	while (_--) {
		printf("Case #%d: ", cas);
		++cas;

		int n;
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i) {
			scanf("%d", &F[i]);
			perm[i] = i;
		}
		int ans = 0;
		do {
			bool flag = 1;
			for (int i = 2; i <= n; ++i) {
				flag = 1;
				memset(sat, 0, sizeof sat);
				for (int k = 2; k < i; ++k) {
					if (perm[k - 1] == F[perm[k]] || perm[k + 1] == F[perm[k]]) {
						sat[k] = 1;
					}
				}
				if (perm[2] == F[perm[1]] || perm[i] == F[perm[1]]) sat[1] = 1;
				if (perm[1] == F[perm[i]] || perm[i - 1] == F[perm[i]]) sat[i] = 1;
 
				for (int k = 1; k <= i; ++k) {
					if (!sat[k]) {
						flag = 0;
						break;
					}
				}
				if (flag) ans = max(ans, i);
			}
		} while (next_permutation(perm + 1, perm + n + 1));
		printf("%d\n", ans);
	}
	return 0;
}