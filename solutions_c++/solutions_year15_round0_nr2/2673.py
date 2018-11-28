#include <iostream>
#include <cstdio>
using namespace std;
const int Maxn = 1010;
int T, n;
int p[Maxn];

bool check(int ans) {
	for (int i = 1; i <= ans; ++i) {
		int sum = 0;
		for (int j = 0; j < n; ++j) {
			sum += (p[j] - 1) / i;
		}
		if (sum + i <= ans) return true;
	}
	return false;
	
}

int solve()
{
	int l = 1, r = 1000;
	while (l <= r) {
		int mid = l + r >> 1;
		if (check(mid)) r = mid - 1;
		else l = mid + 1;
	}
	return l;
}
int main()
{
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", p + i);
		
		printf("Case #%d: %d\n", cas, solve());
	}
	return 0;
}