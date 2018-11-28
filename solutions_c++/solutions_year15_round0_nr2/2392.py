#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <cctype>
#include <queue>
#include <complex>
#include <functional>
#include <sstream>
#include <tuple>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin >> tn;
    for (int tc = 0; tc < tn; tc++)
    {
    	int n;
    	cin >> n;
    	vector<int> a(n);
    	for (int i = 0; i < n; i++)
    		cin >> a[i];
    	int best = 1000;
    	for (int m = 1; m <= 1000; m++)
    	{
    		int cnt = 0;
    		for (int i = 0; i < n; i++)
    			cnt += (a[i] - 1) / m;
    		best = min(best, m + cnt);
    	}
    	cout << "Case #" << tc + 1 << ": " << best << endl;
    }
    return 0;
}