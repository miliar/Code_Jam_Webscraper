#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

int N;
int V;
int X;

int rs[110];	// 속도
int cs[110];	// 온도

double solve()
{
	if (N>=3)
	{
		return -1;
	}

	if (N==1)
	{
		if (cs[0] != X)
		{
			return -1;
		}
		else
		{
			return (double)V / rs[0];
		}
	}

	// N == 2
	if (cs[0] > cs[1])
	{
		swap(cs[0], cs[1]);
		swap(rs[0], rs[1]);
	}

	// cs[0] <= cs[1]
	if (cs[0] == cs[1])
	{
		if (cs[0] != X)
		{
			return -1;
		}
		else
		{
			return (double)V / (rs[0] + rs[1]);
		}
	}

	// cs[0] < cs[1]
	if (cs[0] == X)
	{
		return (double)V / rs[0];
	}
	else if (cs[1] == X)
	{
		return (double)V / rs[1];
	}
	else if ((cs[0] < X && cs[1] < X)
		|| (cs[0] > X && cs[1] > X))
	{
		return -1;
	}

	// cs[0] < X < cs[1]
	int sum = (X - cs[0]) + (cs[1] - X);
	double v0 = (double)V * (cs[1] - X) / sum;
	double v1 = (double)V * (X - cs[0]) / sum;

	return max(v0 / rs[0], v1 / rs[1]);
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int tc=1; tc<=t; ++tc)
	{
		int v1, v2, x1, x2;
		scanf("%d %d.%d %d.%d", &N, &v1, &v2, &x1, &x2);
		V = v1 * 10000 + v2;
		X = x1 * 10000 + x2;

		for (int i=0; i<N; ++i)
		{
			scanf("%d.%d %d.%d", &v1, &v2, &x1, &x2);
			rs[i] = v1 * 10000 + v2;
			cs[i] = x1 * 10000 + x2;
		}
		
		printf("Case #%d: ", tc);

		double ans = solve();
		if (ans < 0)
		{
			printf("IMPOSSIBLE");
		}
		else
		{
			printf("%.10f", ans);
		}

		printf("\n");
	}
	
	return 0;
}