#include <bits/stdc++.h>
using namespace std;
void iosInit() {ios_base::sync_with_stdio(false); cin.tie(nullptr);}

bool check(int N, bool* a) {
	while (N) {
		a[N % 10] = true;
		N /= 10;
	}
	for (int i = 0; i < 10; ++i) if (!a[i]) return false;
	return true;
}

int solve(int N) {
	if (N == 0) return -1;
	bool a[10] = {false};
	int res = N;
	while (1) {
		if (check(res, a)) break;
		res += N;
	}
	return res;
}

int main() {
	int T, N;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		scanf("%d", &N);
		printf("Case #%d: ", i);
		int ans = solve(N);
		if (ans < 0) puts("INSOMNIA");
		else printf("%d\n", ans);
	}
	return 0;
}
