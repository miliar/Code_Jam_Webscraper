#include <bits/stdc++.h>

typedef long long LLONG;

inline void execState(int& state, LLONG value) {
	for (; value; value /= 10) {
		int v = value % 10;
		state |= 1 << v;
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, n, tt = 0;
	scanf("%d", &t);
	for (; t--;) {
		printf("Case #%d: ", ++tt);
		LLONG answer = 0;
		scanf("%d", &n);
		if (!n) {
			puts("INSOMNIA");
			continue;
		}
		LLONG cur = 0;
		int curState = 0;
		for (int i = 1; ; ++i) {
			cur += n;
			execState(curState, cur);
			if (1023 == curState) {
				answer = cur;
				break;
			}
		}
		//std::cout<<answer<<std::endl;
		printf("%I64d\n", answer);
	}
	return 0;
}
