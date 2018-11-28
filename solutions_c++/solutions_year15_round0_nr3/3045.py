#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

typedef pair<int, int> PII;

char s[11111];

PII mul(PII a, PII b) {
	int y = a.second ^ b.second;
	if (a.first == 0) return make_pair(b.first, y);
	if (b.first == 0) return make_pair(a.first, y);
	if (a.first == b.first) return make_pair(0, y ^ 1);
	if (a.first == 1 && b.first == 2) return make_pair(3, y);
	if (a.first == 1 && b.first == 3) return make_pair(2, y ^ 1);
	if (a.first == 2 && b.first == 1) return make_pair(3, y ^ 1);
	if (a.first == 2 && b.first == 3) return make_pair(1, y);
	if (a.first == 3 && b.first == 1) return make_pair(2, y);
	if (a.first == 3 && b.first == 2) return make_pair(1, y ^ 1);

	return make_pair(0, 0);
}

void work() {
	int n, m; scanf("%d%d", &n, &m);
	scanf("%s", s);

	int flag = 0; PII cur = make_pair(0, 0);

	for (int t = 0; t < m; ++t)
		for (int i = 0; i < n; ++i) {
			PII x = make_pair(0, 0);
			if (s[i] == 'i') x.first = 1;
			if (s[i] == 'j') x.first = 2;
			if (s[i] == 'k') x.first = 3;

			cur = mul(cur, x);

			if (cur.first == 1 && cur.second == 0 && flag == 0) flag = 1;

			if (cur.first == 3 && cur.second == 0 && flag == 1) flag = 2;

			//printf("%d, %d\n", cur.first, cur.second);
		}

	if (flag == 2 && cur.first == 0 && cur.second == 1) puts("YES"); else puts("NO");
}

int main() {
	int T; scanf("%d", &T);

	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		work();
	}

	return 0;
}
