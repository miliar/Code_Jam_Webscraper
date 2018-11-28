#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <unordered_set>

using namespace std;
typedef long long ll;
const double eps = 1e-9;
const ll mod = 1e9 + 7;





int main(){
	freopen("B-small-attempt1 (2).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
		
		int n;
		cin >> n;
		double v, x;
		cin >> v >> x;
		vector<pair<double, double > > q(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> q[i].first >> q[i].second;
		}

		if (n == 1)
		{
			if (q[0].second != x)
			{
				//cout << "IMPOSSIBLE\n";
				printf("Case #%d: IMPOSSIBLE\n", t);
			}
			else
			{
				double ans = v / q[0].first;
				printf("Case #%d: %.7lf\n", t, ans);
			}
		}
		else
		{
			if (q[0].second > x && q[1].second > x || q[0].second < x && q[1].second < x)
			{
				printf("Case #%d: IMPOSSIBLE\n", t);
			}
			else
			{
			
				double v1, v2, ans;
				if (q[0].second != q[1].second)
				{
					v2 = (x - q[0].second) / (q[1].second - q[0].second);
					v1 = 1 - v2;
					ans = max(v*v1 / q[0].first, v*v2 / q[1].first);
				}
				else
				{
					ans = v / (q[0].first + q[1].first);
				}
				
				printf("Case #%d: %.7lf\n", t, ans);
			}
		}


	}


	return 0;
}
/*
6
1 10.0000 50.0000
0.2000 50.0000
2 30.0000 65.4321
0.0001 50.0000
100.0000 99.9000
2 5.0000 99.9000
30.0000 99.8999
20.0000 99.7000
2 0.0001 77.2831
0.0001 97.3911
0.0001 57.1751
2 100.0000 75.6127
27.0364 27.7990
70.0263 75.6127
2 100.0000 75.6127
70.0263 75.6127
27.0364 27.7990

*/