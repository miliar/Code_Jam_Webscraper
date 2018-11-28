#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cstdlib>
#include<ctime>
#include<cassert>

using namespace std;

#define FNAME "1"
#define FILE 1

#define pb push_back
#define mp make_pair
#define LL long long
#define ULL unsigned long long
#define LD long double

#ifdef WIN32
	#define I64 "%I64d"
#else
	#define I64 "%lld"
#endif

const int INF = 1e9;

int T, n, a[1005], b[1005], d[1005][1005], x, it, ans, min1;

int main()
{
	#if (FILE == 1)
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout);
	#endif
	scanf("%d", &T);
	for (int g = 0; g < T; g++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
			b[i] = a[i];
		}
		for (int i = 0; i < n; i++)
			for (int j = 0; j <= n; j++)
				d[i][j] = INF; 
		sort(b, b + n);
		for (int i = 0; i < n; i++)
		{
			ans = 0;
			x = b[i];
			for (int j = 0; j < n; j++)
			{
				if (x == a[j])
				{
					it = j;
					break;	
				}
				if (x < a[j])
					ans++;
			}
			for (int j = 0; j <= i + 1; j++)
			{
				if (i == 0)
				{
					if (j == 0)
						d[i][j] = n - 1 - ans;
					else
						d[i][j] = ans;
					continue;
				}
				d[i][j] = d[i - 1][j] + n - i - 1 - ans;
				if (j != 0)
					d[i][j] = min(d[i][j], d[i - 1][j - 1] + ans);
			}
		}
		/*for (int i = 0; i < n; i++)
		{
			for (int j = 0; j <= i + 1; j++)
				printf("%d ", d[i][j]); 
			puts("");
		}*/
		min1 = INF;
		for (int i = 0; i <= n; i++)
			min1 = min(min1, d[n - 1][i]);
		printf("Case #%d: %d\n", g + 1, min1);
	}
	return 0;
}