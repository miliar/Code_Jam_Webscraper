#include <stdio.h>
#include <algorithm>

using namespace std;

const int MAXN = 10010;
int n, x;
int s[MAXN];
int ans;

void init()
{
	scanf("%d%d", &n, &x);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &s[i]);
	}
}

void solve()
{
	sort(s, s + n);
	ans = 0;
	int i = 0, j = n - 1;
	while (i < j) {
		if (s[i] + s[j] <= x) ++i, --j, ++ans;
		else --j, ++ans;
	}
	if (i == j) ++ans;
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
