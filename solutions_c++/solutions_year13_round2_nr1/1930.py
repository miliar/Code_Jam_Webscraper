#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <vector>

using namespace std;

#define ll long long

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	int s, n;
	vector<int> v;

	scanf("%d", &tests);

	for (int t = 0; t < tests; t++) {
		scanf("%d %d", &s, &n);

		v.clear();
		v.resize(n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &v[i]);
		}

		sort(v.begin(), v.end());

		if (s == 1) {
			printf("Case #%d: %d\n", t + 1, n);
			continue;
		}

		int ans = 2000000000;
		int currAns = 0;
		ll curr = s;
		for (int i = 0; i < n; i++) {
			ans = min(ans, currAns + n - i);

			while (curr <= v[i]) {
				curr = curr + curr - 1;
				currAns++;
			}

			curr += v[i];
		}

		ans = min(ans, currAns);

		printf("Case #%d: %d\n", t + 1, ans);
	}


	return 0;
}
/*
4
2 2
2 1
2 4
2 1 1 6
10 4
25 20 9 100
1 4
1 1 1 1

1
2 10
100 100 100 100 100 100 100 100 100 100
*/