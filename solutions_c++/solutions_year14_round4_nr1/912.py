#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
const int MAXN = 10010;

int a[MAXN];

int main() {
	int T;
	freopen("x.txt", "r", stdin);freopen("w.txt", "w", stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		int N, X;
		scanf("%d%d", &N, &X);
		for (int i = 0; i < N; i++) {
			scanf("%d", a + i);
		}
		sort(a, a + N);
		int j = 0;
		int ans = 0;
		for (int i = N - 1; i >= j; i--) {
			ans++;
			if (X - a[i] >= a[j]) {
				j++;
			}
		}
		printf("Case #%d: %d\n", cas, ans);
	}
}
