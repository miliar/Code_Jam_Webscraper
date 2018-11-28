#include <cstdio>
int a[1000000];
void solve() {
	int n, P, Q, R, S;
	scanf("%d%d%d%d%d", &n, &P, &Q, &R, &S);
	long long sum = 0;
	for (int i = 0; i < n; i++)
		a[i] = (1LL*i*P+Q)%R+S, sum += a[i];
	long long l = (sum+2)/3, r = sum;
	while (l < r) {
		long long mid = l+r>>1, tmp;
		int j = 0;
		for (int i = 0; i < 3; i++) {
			tmp = 0;
			for (; j < n && tmp + a[j] <= mid; tmp += a[j], j++);
		}
		if (j == n) r = mid;
		else l = mid+1;
	}
	printf("%.10lf\n", 1-1.0*l/sum);
}
int main() {
	int T; scanf("%d", &T);
	for (int _ = 1; _ <= T; _++)
		printf("Case #%d: ", _), solve();
	return 0;
}
