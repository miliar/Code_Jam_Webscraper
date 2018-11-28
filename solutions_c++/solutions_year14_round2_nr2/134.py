#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void work() {
	long long A, B, C; cin >> A >> B >> C; long long ans = 0;
	for (long long a = 0; a < A; ++a)
		for (long long b = 0; b < B; ++b)
			if ((a & b) < C) ans++;
	cout << ans << endl;
}

int main() {
	int T; scanf("%d", &T);

	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		work();
	}

	return 0;
}
