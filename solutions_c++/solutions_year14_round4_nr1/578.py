#include <cstdio>
#include <algorithm>

int N;
int arr[10001];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int X;
		scanf("%d%d", &N, &X);
		for (int i = 0; i < N; ++i)
			scanf("%d", &arr[i]);
		std::sort(arr, arr + N);
		int ans = 0;
		int l = 0, r = N;
		while (l < r) {
			if (arr[r - 1] + arr[l] > X) {
				++ans;
				--r;
			} else {
				++ans;
				--r;
				++l;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}

}