#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>

#define INF 2147483647
#define PI acos(-1.0)

using namespace std;

int GO[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
map<char, int> M = {{'^', 0}, {'>', 1}, {'v', 2}, {'<', 3}};

int main(int argc, const char ** argv)
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;

	for(int _t = 1; _t <= tests; ++_t)
	{

		int n;
		double v, x;
		cin >> n >> v >> x;
		vector <double> V(n), X(n);
		for(int i = 0; i < n; ++i)
			cin >> V[i] >> X[i];

		bool same = true;
		for(int i = 1; i < n; ++i)
			if(X[i] != X[0])
				same = false;

		if(same)
		{
			if(X[0] == x)
			{
				double sum = 0.0;
				for(int i = 0; i < n; ++i)
					sum += V[i];
				printf("Case #%d: %.10lf\n", _t, v / sum);
			}
			else
			{
				printf("Case #%d: IMPOSSIBLE\n", _t);
			}
			continue;
		}

		double t0 = v * (x - X[0]) / V[1] / (X[1] - X[0]);
		double t1 = v * (x - X[1]) / V[0] / (X[0] - X[1]);

		if(t0 < 0 || t1 < 0)
			printf("Case #%d: IMPOSSIBLE\n", _t);
		else
			printf("Case #%d: %.10lf\n", _t, max(t0, t1));
	}

	return 0;
}
