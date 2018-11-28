#include <cstdio>
#include <algorithm>
using namespace std;
const int nmax = 1000 + 18;

int d[nmax], D;

int check(int k)
{
	int rnt = 0;
	for (int i = 1; i <= D; ++i)
		rnt += (d[i] - 1) / k;
	return rnt + k;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		int ans = 1;
		scanf("%d", &D);
		for (int i = 1; i <= D; ++i)
			scanf("%d", d + i), ans = max(ans, d[i]);
		for (int i = 1; i <= ans; ++i)
			ans = min(ans, check(i));
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}
