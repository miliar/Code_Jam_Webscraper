#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

void solve_small(int s) {
	for(int i=1 ; i<=s ; i++) {
		if (i>1) printf(" ");
		printf("%d", i);
	}
	printf("\n");
}

int main() {

	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++) {
		int k, c, s;
		scanf("%d%d%d", &k, &c, &s);

		printf("Case #%d: ", tc);
		solve_small(s);
	}

	return 0;
}