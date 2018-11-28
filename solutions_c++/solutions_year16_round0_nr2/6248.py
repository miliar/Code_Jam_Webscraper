#include "bits/stdc++.h"
using namespace std;

int kase;

int main() {
	freopen("out", "w", stdout);
	freopen("in", "r", stdin);
	scanf("%d", &kase);
	for (int nCase = 1; nCase <= kase; ++nCase) {
		printf("Case #%d: ", nCase);
		char s[105]; scanf("%s", s);
		int size = strlen(s), res = 0;
		int idx[105], cnt = 0;
		for (int i = 0; i < size; ++i) if (s[i] == '+')
			idx[cnt++] = i;
		if (cnt == 0) { puts("1"); continue; }
		bool f = (idx[0] != 0), h = (idx[cnt - 1] != size - 1);
		for (int i = 0, cntCopy = cnt; i < cntCopy - 1; ++i)
			if (idx[i] + 1 == idx[i + 1]) cnt -= 1;
		res = 2 * (cnt - 1);
		if (f) res += 1;
		if (h) res += 2;
		printf("%d\n", res);
	}
	return 0;
}
