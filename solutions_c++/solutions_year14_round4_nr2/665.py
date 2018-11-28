#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int MAXN = 1010;
int n;
int a[MAXN], b[MAXN];
int ans;

void init()
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
	memcpy(b, a, sizeof(b));
	sort(b, b + n);
}

void solve()
{
	ans = 0;
	int l = 0, r = n - 1;
	for (int i = 0; i < n; ++i) {
		int p = find(a, a + n, b[i]) - a;
		if (p - l < r - p) {
			while (p > l) {
				swap(a[p], a[p - 1]);
				--p; ++ans;
			}
			++l;
		} else {
			while (p < r) {
				swap(a[p], a[p + 1]);
				++p; ++ans;
			}
			--r;
		}
	}
}

int main()
{
	int dat;
	scanf("%d", &dat);
	for (int cas = 1; cas <= dat; ++cas) {
		init();
		solve();
		printf("Case #%d: %d\n", cas, ans);
	}
}
