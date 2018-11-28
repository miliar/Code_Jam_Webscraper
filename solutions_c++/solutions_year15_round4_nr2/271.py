#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <memory.h>


using namespace std;
double EPS = 1e-10;
int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int N;
		double V, X;
		cin >> N >> V >> X;
		vector<pair<double, double> > v;
		double s = 0;
		for (int i = 0; i < N; i++)
		{
			double r, c;
			cin >> r >> c;
			v.push_back(make_pair(c, r));
			s += r;
		}
		sort(v.begin(), v.end());
		reverse(v.begin(), v.end());

		vector<pair<double, double> > vv;
		for (int i = 0; i < N; i++)
			if (i == 0 || v[i-1].first != v[i].first)
				vv.push_back(v[i]);
			else
				vv[vv.size() - 1].second += v[i].second;
		v=vv;
		N = v.size();
		if (v[0].first < X || v[v.size() - 1].first > X)
		{
			printf("Case #%d: IMPOSSIBLE\n", t+1);
		}
		else
		{
			double minT = V / s;
			double maxT = 0;
			for (int i = 0; i < N; i++)
				maxT += V / v[i].second;
			for (int z = 0; z < 150; z++)
			{
				double tt = (minT + maxT) / 2;
				double up = 0;
				double leftUp = V;
				for (int i = 0; i < N; i++)					
					{
						double can = min(v[i].second * tt, leftUp);
						up += can * v[i].first;
						leftUp -= can;
					}

				double down = 0;
				double leftDown = V;
				for (int i = N-1; i >= 0; i--)					
					{
						double can = min(v[i].second * tt, leftDown);
						down += can * v[i].first;
						leftDown -= can;
					}
				if (leftDown <= 0 && leftUp <= 0 && up >= X * V && down <= X * V)
					maxT = tt;
				else
					minT = tt;
			}
			printf("Case #%d: %.8lf\n", t+1, (minT + maxT) / 2);
		}

	}
	return 0;
}