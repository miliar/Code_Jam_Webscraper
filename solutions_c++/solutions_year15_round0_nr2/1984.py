#define _CRT_SECURE_NO_WARNINGS

#pragma comment(linker, "/STACK:100000000")

#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <cstring>
#include <queue>
#include <deque>
#include <functional>
#include <climits>
#include <cassert>
#include <list>

#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))
#define ABS(a) (((a) > 0) ? (a) : (-(a)))
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))

using namespace std;
typedef long long ll;

const int N = 10010;

int dp[N];

int f(int i)
{
	if (dp[i] != -1) return dp[i];
	dp[i] = min(f(i - 1), f(i / 2 + i % 2)) + 1;
	return dp[i];
}

map<vector<int>, int> d;

int tupoe(vector<int> v)
{
	if (v.size() == 0) return 0;

	if (d.find(v) != d.end()) return d[v];
	
	vector<int> paramter = v;
	for (int i = 0; i < paramter.size(); i++)
		paramter[i]--;
	sort(paramter.begin(), paramter.end());
	reverse(paramter.begin(), paramter.end());
	while (paramter.size() && paramter.back() == 0) paramter.pop_back();
	int res = 1e9;
	res = tupoe(paramter) + 1;
	for (int i = 0; i < v.size(); i++)
	{
		for (int k = 1; k < v[i]; k++)
		{
			paramter = v;
			paramter.push_back(paramter[i] - k);
			paramter[i] = k;
			sort(paramter.begin(), paramter.end());
			reverse(paramter.begin(), paramter.end());
			while (paramter.size() && paramter.back() == 0) paramter.pop_back();
			res = min(tupoe(paramter) + 1, res);
		}
	}
	return d[v] = res;
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	NEGATE(dp);
	dp[0] = 0;
	dp[1] = 1;

	int tests;
	cin >> tests;
	for (int q = 0; q < tests; q++)
	{
		int ans = 1e9;
		int d;
		cin >> d;
		vector<int> a;
		for (int i = 0; i < d; i++)
		{
			int x;
			cin >> x;
			a.push_back(x);
		}

		/*for (int i = 0; 1; i++)
		{
			if (a.empty())
			{
				ans = min(ans, i); break;
			}
			int mx = *max_element(a.begin(), a.end());
			ans = min(i + mx, ans);
			if (mx == 1) break;

			if (mx % 2 == 1)
			{
				for (int i = 0; i < a.size(); i++)
					a[i]--;
				for (int i = 0; i < a.size(); i++)
				{
					if (a[i] == 0)
					{
						a.erase(a.begin() + i);
						i--;
					}
				}
				continue;
			}

			a.erase(max_element(a.begin(), a.end()));
			
			int a1 = mx / 2;
			int a2 = mx - a1;

			if (a1)
				a.push_back(a1);
			if (a2)
				a.push_back(a2);
		}*/

		int mx = *max_element(a.begin(), a.end());

		for (int t = 1; t <= mx; t++)
		{
			int cur = 0;
			for (int j = 0; j < a.size(); j++)
			{
				cur += (a[j] - 1) / t;
			}
			ans = min(ans, cur + t);
		}


		cout << "Case #" << q + 1 << ": " << ans << endl;
		/*int d;
		cin >> d;
		vector<int> a(d);
		for (int i = 0; i < d; i++) cin >> a[i];
		cout << "Case #" << q + 1 << ": " << tupoe(a) << endl;*/
	}

	return 0;
}