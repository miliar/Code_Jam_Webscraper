#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>

#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;

const int inf = 0x3f3f3f3f;

int tp = 0;
int T;
int n, K;
double f[205][205];
double p[2005];
double a[2005];

int main( )
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	while (T --)
	{
		scanf("%d %d", &n, &K);
		for (int i = 1; i <= n; i ++)
			scanf("%lf", &p[i]);
		sort(p + 1, p + 1 + n);
		int m = 0;
		double ans = 0.0;
			++ tp;
		for (int r = 0; r <= K; r ++)
		{
			m = 0;
			for (int i = 1; i <= K - r; i ++)
				a[++ m] = p[i];
			for (int i = 1; i <= r; i ++)
				a[++ m] = p[n - i + 1];
	
			memset(f, 0, sizeof(f));
			f[0][0] = 1.;
			for (int i = 0; i < K; i ++)
				for (int j = 0; j <= i; j ++)
				{
					double tmp = a[i + 1];
					f[i + 1][j + 1] += f[i][j] * tmp;
					f[i + 1][j] += f[i][j] * (1 - tmp);
				}
			ans = max(ans, f[K][K / 2]);
		}
		printf("Case #%d: %.9f\n", tp, ans);
	}
	return 0;
}
