#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1000 + 10;
char buf[MAXN];

int main() {
	int T; scanf("%d", &T);
	for (int cas = 1; cas <= T; ++ cas) {
		printf("Case #%d: ", cas);
		int N; scanf("%d%s", &N, buf);
		int ret = 0, now = buf[0] - '0';
		for (int i = 1; i <= N; ++ i) {
			int cnt = buf[i] - '0';
			if (now < i) ret += i - now, now = i;
			now += cnt;
		}
		printf("%d\n", ret);
	}
	return 0;
}
