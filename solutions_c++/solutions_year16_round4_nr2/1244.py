# include <cstdio>
# include <cmath>
# include <cstring>
# include <string>
# include <vector>
# include <queue>
# include <map>
# include <iostream>
# include <algorithm>

using namespace std;

const int MAX_N = 16;

int n, k;
double p[MAX_N];

int m;
double q[MAX_N];

double dist[20];
double cans;

double ans;

void go (int type, int idx, int score, double prob)
{
	if (idx == m)
	{
		dist[8 - score] += prob;
		return;
	}
	if (idx == (m >> 1) && !type)
	{
		cans += prob * dist[8 + score];
		return;
	}
	go (type, idx + 1, score + 1, prob * q[idx]);
	go (type, idx + 1, score - 1, prob * (1.0 - q[idx]));	
}

double solve ()
{
	int i;
	m ++;
	cans = 0;
	for (i = 0; i < MAX_N; i ++)
		dist[i] = 0;
	go (1, m >> 1, 0, 1);
	go (0, 0, 0, 1);
	///printf ("--%lf\n", cans);
	return cans;
}


int main ()
{
	int nt, t, i, j;
	scanf ("%d", &t);
	for (nt = 1; nt <= t; nt ++)
	{	
		ans = 0.0;
		printf ("Case #%d: ", nt);
		scanf ("%d%d", &n, &k);
		for (i = 0; i < n; i ++)
			scanf ("%lf", &p[i]);
		for (i = 1; i < (1 << n); i ++)
		{
			m = -1;
			for (j = 0; j < n; j ++)
			{
				if (i & (1 << j))
					q[++ m] = p[j];
			}
			if ((m + 1) != k)
				continue;
			/**
			for (j = 0; j <= m; j ++)
				printf ("%lf ", q[j]);
			printf ("\n");
			**/
			ans = max (ans, solve ());
		}
		printf ("%.9lf\n", ans);
	}
	return 0;
}

