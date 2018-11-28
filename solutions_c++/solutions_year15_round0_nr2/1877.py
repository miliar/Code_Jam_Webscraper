#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <vector>

using namespace std;

vector <int> v;



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	ios_base::sync_with_stdio(0);
	for (int i = 1; i <= t; i++)
	{
		int n;
		cin >> n;
		v.clear();
		for (int j = 1; j <= n; j++)
		{
			int x;
			cin >> x;
			v.push_back(x);
		}
		int cur = 1000;
		for (int j = 1; j <= 1000; j++)
		{
			int ans = 0;
			for (int pp = 0; pp < n; pp++)
			{
				if (v[pp] % j == 0)
				{
					ans += v[pp] / j;
					ans--;
				}
				else
				{
					ans += v[pp] / j;
				}
			}
			cur = min(cur, ans + j);
		}
		cout << "Case #" << i << ": " << cur << "\n";
	}


	return 0;
}