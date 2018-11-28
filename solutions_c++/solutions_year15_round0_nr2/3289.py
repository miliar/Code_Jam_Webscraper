#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 2000;

int n;
int p[N];

int main() {
	freopen("Blarge.in", "r", stdin);
	freopen("Blarge.out", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int cas = 1; cas <= test; cas++) {
		printf("Case #%d: ", cas);
		scanf("%d", &n);
		int ok = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &p[i]);
			if (p[i]) ok = 1;
		}
		int ans = 1000;
		for (int i = 1; i <= 1000; i++) {
			int s = i;
			for (int j = 0; j < n; j++)
				s += (p[j]-1)/i;
			ans = min(ans, s);
		}
		if (!ok) ans = 0;
		cout << ans << endl;
	}
}
