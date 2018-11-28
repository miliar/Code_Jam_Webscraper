#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long lint;
typedef vector<int> vi;
typedef vector<string> vs;
const int INF = 0x7fffffff;

bool les(vi &a, vi &b)
{
	for(int i = 0; i < a.size(); ++i)
		if(a[i] == b[i])
			continue;
		else if(a[i] < b[i])
			return true;
		else 
			return false;
	return true;
}

bool equal(vi &a, vi &b)
{
	for(int i = 0; i < a.size(); ++i)
		if(b[i] != a[i])
			return false;
	return true;
}

int Solution()
{
	int n, k;
	cin >> k >> n;

	vector< pair< vector<int>, vector<int> > > dp(vector<pair<vector<int>, vector<int> > >((1 << n) + 1, 
			make_pair(vector<int>(201, 0), vector<int>())));
	for(int i = 0; i < k; ++i)
	{
		int key;
		cin >> key;
		dp[0].first[key]++;
	}

	vector<int> open(n + 1);
	vector<vector<int> > keys(n + 1);
	for(int i = 1; i <= n; ++i)
	{
		cin >> open[i];
		int cnt;
		cin >> cnt;
		keys[i].resize(cnt);
		for(int j = 0; j < cnt; ++j)
			cin >> keys[i][j];
	}

	for(int i = 0; i < (1 << n); ++i)
	{
		if(i > 0 && dp[i].second.size() == 0)
			continue;

		for(int j = 0; j < n; ++j)
		{
			if(i & (1 << j))
				continue;
			if(dp[i].first[ open[j + 1] ] < 1)
				continue;
			vector<int> newWay = dp[i].second;
			newWay.push_back(j + 1);
			if(dp[i + (1 << j)].second.size() != 0 && !les(newWay, dp[i + (1 << j)].second))
				continue;

			dp[i + (1 << j)] = dp[i];
			dp[i + (1 << j)].second = newWay;
			dp[i + (1 << j)].first[ open[j + 1] ]--;
			for(int x = 0; x < keys[j + 1].size(); ++x)
				dp[i + (1 << j)].first[ keys[j + 1][x] ] ++;
		}
	}

	if(dp[(1 << n) - 1].second.size() == 0)
	{
		cout << "IMPOSSIBLE";
		return 0;
	}
	
	for(int i = 0; i < n; ++i)
		cout << dp[(1 << n) - 1].second[i] << ' ';

	return 0;
}

#define debug 1

int main()
{
#ifdef debug
	freopen("D-small-attempt5.in", "r", stdin);
	freopen("D-small-attempt5.out", "w", stdout);
#endif
	int n;
	cin >> n;
	getchar();
	for(int i = 1; i <= n; ++i)
	{
		printf("Case #%d: ", i);
		Solution();
		printf("\n");
	}
	return 0;
}
