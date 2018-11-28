#include <functional>
#include <algorithm>
#include <strstream>
#include <iostream>
#include <numeric>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int main()
{
	freopen("b_large.in", "r", stdin);
	freopen("b_large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		int n;
		cin >> n;
		vector<int> v(n);
		for (int& x : v)
			cin >> x;
		
		int ans = 1000000000;

		for (int lm = 1; lm <= 1000; ++lm)
		{
			int tmp = 0;
			for (int i = 0; i < n; ++i)
				tmp += (v[i] + lm - 1) / lm - 1;
			ans = min(ans, tmp + lm);
		}


		cout << "Case #" << i << ": " << ans << endl;
	}

	return 0;
}