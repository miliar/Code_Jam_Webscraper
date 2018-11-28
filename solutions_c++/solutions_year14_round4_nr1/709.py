#include <cstdio>
#include <iostream>
#include <set>
#include <functional>
#include <vector>

using namespace std;

int nTest;
int n, X;
int s[100010];
multiset<int> S;

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("O.txt", "w", stdout);

	scanf("%d", &nTest);
	for (int test = 1; test <= nTest; test++) {
		scanf("%d%d", &n, &X);
		S.clear();
		for (int i = 1; i <= n; i++) {
			scanf("%d", s + i);
			S.insert(-s[i]);
		}

		int ret = 0;
		while (!S.empty()) {
			int A = *S.begin(); S.erase(S.begin());
			multiset<int>::iterator it = S.lower_bound(-(X + A));
			if (it != S.end()) 
				S.erase(it);
			ret++;
		}
		printf("Case #%d: %d\n", test, ret);
	}

	return 0;

}