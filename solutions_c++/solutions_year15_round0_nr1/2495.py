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

int solve()
{
	int n;
	string s;
	cin >> n >> s;
	int ans = 0;
	int cur = 0;
	for (int i = 0; i < s.size(); ++i)
	{
		s[i] -= '0';
		ans += max( 0, i - cur );
		cur += max( 0, i - cur ) + s[i];
	}
	return ans;
}

int main()
{
	freopen("a_large_0.in", "r", stdin);
	freopen("a_large_0.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i )
		cout << "Case #" << i << ": " << solve() << endl;
	return 0;
}