#include <cstdio>
#include <cstring>
#include <set>

using namespace std;

int val[0x100];
set<int> b[2];

void print(set<int> s) {
	for (set<int>::iterator it = s.begin(); it != s.end(); ++it) {
		printf("%d ", *it);
	}
	printf("\n");
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++cas) {
		int c, d, v;
		scanf("%d%d%d", &c, &d, &v);
		for (int i = 0; i < d; ++i) {
			scanf("%d", &val[i]);
		}

		b[0].clear();
		b[1].clear();
		int tag = 0;
		for (int i = 0; i < d; ++i) {
			b[tag].insert(val[i]);
			for (set<int>::iterator it = b[tag ^ 1].begin(); it != b[tag ^ 1].end(); ++it) {
				if (val[i] + *it > v) break;
				b[tag].insert(val[i] + *it);
			}
			//printf("after insert %d:\n", val[i]);
			//print(b[tag]);
			b[tag ^ 1] = b[tag];
			tag = tag ^ 1;
		}

		int ret = 0;
		for (int i = 1; i <= v; ++i) {
			if (b[tag ^ 1].find(i) == b[tag ^ 1].end()) {
				++ret;
				b[tag ^ 1].insert(i);
				for (set<int>::iterator it = b[tag].begin(); it != b[tag].end(); ++it) {
					if (i + *it > v) break;
					b[tag ^ 1].insert(i + *it);
				}
				b[tag] = b[tag ^ 1];
				tag = tag ^ 1;
			}
		}
		printf("Case #%d: %d\n", cas, ret);
	}
	return 0;
}

