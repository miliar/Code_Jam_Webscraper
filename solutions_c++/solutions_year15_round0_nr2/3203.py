#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

vector <int> dishes;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int ans = INF;
		dishes.clear();
		int d;
		cin >> d;
		int max_p = -229;
		for (int j = 0; j < d; j++)
		{
			int a;
			cin >> a;
			max_p = max(max_p, a);
			dishes.push_back(a);
		}
		for (int j = 1; j <= max_p; j++)
		{
			int cur_ans = j;
			for (int k = 0; k < d; k++)
			{
				cur_ans += ((dishes[k] + j - 1) / j) - 1;
			}
			ans = min(ans, cur_ans);
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}