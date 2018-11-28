#pragma comment (linker, "/STACK:268435456")
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <cmath>
#include <cctype>
#include <sstream>
#include <ctime>
#include <tuple>
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
using namespace std;
template <typename T> using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
template <typename T> T sqr(T r) { return r * r; }

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin >> tn;
    for (int tc = 0; tc < tn; tc++)
    {
    	double x, v;
    	int n;
    	cin >> n >> v >> x;
    	vector<double> r(n), c(n);
    	for (int i = 0; i < n; i++)
    		cin >> r[i] >> c[i];
    	double result;
    	int fail = 1;
    	if (n == 1)
    	{
    		fail = fabs(c[0] - x) > 1e-10;
    		result = v / r[0];
    	}
    	else
    	{
    		if (c[0] > c[1])
    		{
    			swap(c[0], c[1]);
    			swap(r[0], r[1]);
    		}
    		fail = x + 1e-10 < c[0] || c[1] + 1e-10 < x;
    		if (!fail)
    		{
    			if (fabs(c[0] - c[1]) < 1e-10)
    				result = v / (r[0] + r[1]);
    			else
    			{
	    			double p0 = (x - c[0]) / (c[1] - c[0]);
	    			double p1 = (c[1] - x) / (c[1] - c[0]);
	    			double t0 = v * p1 / r[0];
	    			double t1 = v * p0 / r[1];
	    			result = max(t0, t1);
	    		}
    		}
    	}
    	cout << "Case #" << tc + 1 << ": ";
    	if (fail)
    		cout << "IMPOSSIBLE";
    	else
    		printf("%0.14lf", result);
    	cout << endl;
    }
    return 0;
}