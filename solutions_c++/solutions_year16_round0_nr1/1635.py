#include <cstdio>
#include <iostream>
#include <set>

using namespace std;

int solve(int n) {
	int ret = -1;
	set<int> S;

	for(int i=1 ; i<1000 ; i++) {
		int x = i * n;
		while(x > 0) {
			S.insert(x%10);
			x /= 10;
		}

		if (S.size() == 10) {
			ret = i * n;
			break;
		}			
	}

	return ret;
}

int main() {

	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", tc);

		if (n == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		
		int ans = solve(n);
		printf("%d\n", ans);
	}

	return 0;
}