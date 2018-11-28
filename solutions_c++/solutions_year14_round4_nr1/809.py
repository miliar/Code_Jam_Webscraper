#include <cstdio>
#include <iostream>
#include <string.h>
#include <cstring>
#include <algorithm>
//using namespace std;
const int maxn = 500010;

int n, m, testnum, c;
int a[maxn];

using namespace std;

bool cmp(int a, int b) {
	return a > b;
}

int main() {
	freopen("A-large.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testnum);

	for (int test = 1; test <= testnum; test++) {
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i++) {
			scanf("%d", &a[i]);
		}
		sort(a + 1, a + 1 + n, cmp);

		int nn = n;
		int ans = 0;
		
		for (int i = 1; i <= nn; i++) {
			int j = a[i]; ans++;
			if (nn > i) {
				if (j + a[nn] <= m) nn--;
			}
		}
		
		printf("Case #%d: %d\n", test, ans);
	}
}