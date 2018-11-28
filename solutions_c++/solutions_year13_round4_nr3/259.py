#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 30;

int n;
int A[MAXN], B[MAXN];

int ans[MAXN];

int found;

int search(int i) {
	if (i > n) {
		return true;
	}

/*
	printf("i = %d\n", i);
	printf("ans =");
	for (int j = 1; j <= n; ++j) printf(" %d", ans[j]);
	printf("\n");
*/	
	int a[MAXN], b[MAXN];
	memset(a, 0, sizeof(a));
	memset(b, 0, sizeof(b));
	for (int x = 1; x <= n; ++x) 
		if (ans[x] < i) {
			a[x] = 1;
			for (int y = 1; y < x; ++y)
				if (ans[y] < ans[x] && a[y] + 1 > a[x]) a[x] = a[y] + 1;
		}
	for (int x = n; x >= 1; --x) 
		if (ans[x] < i) {
			b[x] = 1;
			for (int y = x + 1; y <= n; ++y)
				if (ans[y] < ans[x] && b[y] + 1 > b[x]) b[x] = b[y] + 1;
		}
/*	
	printf("a =");
	for (int j = 1; j <= n; ++j) printf(" %d", a[j]);
	printf("\n");
	printf("b =");
	for (int j = 1; j <= n; ++j) printf(" %d", b[j]);
	printf("\n");
*/	

	for (int j = 1; j <= n; ++j) {
		if (ans[j] > n) {
			int fa = 1, fb = 1;
			for (int x = 1; x < j; ++x) 
				if (a[x] + 1 > fa) fa = a[x] + 1;
			for (int x = j+1; x <= n; ++x)
				if (b[x] + 1 > fb) fb = b[x] + 1;
			if (A[j] == fa && B[j] == fb) {
				ans[j] = i;
				if (search(i + 1)) return true;
				ans[j] = n + 1;
			}
		}
	}

	return false;
}

void solve() {
	for (int i = 1; i <= n; ++i)
		ans[i] = n + 1;

	search(1);

	for (int i = 1; i <= n; ++i) {
		if (i > 1) printf(" ");
		printf("%d", ans[i]);
	}
	printf("\n");
}

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d", &t);
	for (int cs = 1; cs <= t; ++cs) {
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i) {
			scanf("%d", A + i);
		}
		for (int i = 1; i <= n; ++i) {
			scanf("%d", B + i);
		}
		printf("Case #%d: ", cs);
		solve();
	}
	return 0;
}