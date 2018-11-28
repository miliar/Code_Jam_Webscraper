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

map<pair<int, int>, vector<int>> mp;

int main()
{
	freopen("c_small_0.in", "r", stdin);
	freopen("c_small_0.out", "w", stdout);

	mp[make_pair(1, 1)] = { 2, 3, 4 };
	mp[make_pair(1, 2)] = { 3, 4 };
	mp[make_pair(1, 3)] = { 2, 3, 4 };
	mp[make_pair(1, 4)] = { 3, 4 };
	mp[make_pair(2, 2)] = { 3, 4 };
	mp[make_pair(2, 3)] = { 4 };
	mp[make_pair(2, 4)] = { 3, 4 };
	mp[make_pair(3, 3)] = { 2, 4 };
	mp[make_pair(3, 4)] = {};
	mp[make_pair(4, 4)] = { 3 };

	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		int x, n, m;
		cin >> x >> n >> m;
		vector<int> v = mp[make_pair(min(n, m), max(n, m))];
		string ans;
		if (find(v.begin(), v.end(), x) != v.end())
			ans = "RICHARD";
		else
			ans = "GABRIEL";
		

		cout << "Case #" << i << ": " << ans << endl;
	}

	return 0;
}