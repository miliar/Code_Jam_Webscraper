#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

char dic[0x100], tar[0x100], buf[0x100];
int nD, nT, nL, cnt, mt;

int cal() {
	int ret = 0;
	for (int i = 0; i <= nL - nT; ++i) {
		bool tag = true;
		for (int j = 0; j < nT; ++j) {
			if (buf[i + j] != tar[j]) {
				tag = false;
				break;
			}
		}
		if (tag) ++ret;
	}
	return ret;
}

void dfs(int pos) {
	if (pos == nL) {
		int tmp = cal();
/*
		if (tmp > 0) {
		buf[pos] = 0;
		printf("get: %s\n", buf);
		printf("  # = %d\n", tmp);
		}
*/
		mt = max(tmp, mt);
		cnt += tmp;
		return;
	}

	for (int i = 0; i < nD; ++i) {
		buf[pos] = dic[i];
		dfs(pos + 1);
	}
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++cas) {
		scanf("%d%d%d", &nD, &nT, &nL);
		scanf("%s", dic);
		scanf("%s", tar);
		int tot = 1;
		for (int i = 0; i < nL; ++i) {
			tot *= nD;
		}
		cnt = mt = 0;
		dfs(0);
		double ret = mt - cnt * 1.0 / tot;
		printf("Case #%d: %.8lf\n", cas, ret);
	}
	return 0;
}

