#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>
#include <cstdint>
#include <cmath>
#include <iostream>
using namespace std;
const int maxn = 16;
int n;
char a[maxn];
int id[maxn];

void init() {
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++) {
		while (true) {
			a[i] = getchar();
			if (a[i] != '\n') {
				break;
			}
		}
		scanf("%d", &id[i]);
	}
}

int count(int k) {
	int tk = k;
	int ans = 0;
	while (true) {
		if (tk == 0) {
			break;
		}
		if ((tk % 2) == 1) {
			ans++;
		}
		tk /= 2;
	}
	return ans;
}

void calc() {
	map<int, int> order;
	int cur = 0;
	for (int i = 0; i < n; i++) {
		if (order.find(id[i]) != order.end()) {
			continue;
		}
		order[id[i]] = cur;
		cur++;
	}
	int f[1 << n];
	for (int i = 0; i < (1 << n); i++) {
		f[i] = count(i);
	}
	for (int i = 0; i < n; i++) {
		int tf[1 << n];
		memset(tf, 0xff, sizeof(tf));
		if (a[i] == 'E') {
			for (int j = 0; j < (1 << n); j++) {
				if (tf[j] < 0) {
					continue;
				}
				int st, en;
				if (id[i] > 0) {
					st = en = order[id[i]];
				} else {
					st = 0;
					en = n - 1;
				}
				for (int k = st; k <=en; k++) {
					if ((j & (1 << k))) {
						continue;
					}
					if (tf[j + (1 << k)] < 0) {
						tf[j + (1 << k)] = f[j] + 1;
					}
					tf[j + (1 << k)] = min(tf[j + (1 << k)], f[j] + 1);
				}
			}
		} else {
			for (int j = 0; j < (1 << n); j++) {
				if (f[j] < 0) {
					continue;
				}
				int st, en;
				if (id[i] > 0) {
					st = en = order[id[i]];
				} else {
					st = 0;
					en = n - 1;
				}
				for (int k = st; k <= en; k++) {
					if ((j & (1 << k)) == 0) {
						continue;
					}
					if (tf[j - (1 << k)] <= 0) {
						tf[j - (1 << k)] = f[j] - 1;
					}
					tf[j - (1 << k)] = min(tf[j - (1 << k)], f[j] - 1);
				}

			}
		}
		for (int j = 0; j < (1 << n); j++) {
			f[j] = tf[j];
		}
	}
	int ans = -1;
	for (int i = 0; i < (1 << n); i++) {
		if (ans < 0) {
			ans = f[i];
		}
		ans = min(ans, f[i]);
	}
	if (ans < 0) {
		printf("CRIME TIME\n");
	} else {
		printf("%d\n", ans);
	}
}

int main() {
	int tcase;
	scanf("%d", &tcase);
	for (int i = 1; i <= tcase; i++) {
		init();
		printf("Case #%d: \n", i);
		calc();
	}
	return 0;
}