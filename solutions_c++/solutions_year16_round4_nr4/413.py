#include <cstdio>
#include <vector>
#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <string.h>
#include <algorithm>
#include <iomanip>
using namespace std;

#pragma comment(linker, "/STACK:99999999999")


int n;
int a[15][15];
char s[15][15];
bool go[15][10000];

vector <int> duo(int x, int sz)
{
	vector <int> ans;
	while (x > 0)
	{
		ans.push_back(x % 2);
		x /= 2;
	}
	while (ans.size() < sz)
		ans.push_back(0);
	return ans;
}
bool can(vector<int> &p) {
	for (int i = 0; i < 15; i++)
	for (int j = 0; j < 1000; j++)
		go[i][j] = false;
	int h = 1;
	for (int i = 0; i < n; i++)
		h *= 2;
	go[0][0] = true;
	for (int i = 0; i < n; i++) {
		for (int mask = 0; mask < h; mask++) {
			vector <int> w = duo(mask, n);
			if (!go[i][mask]) continue;
			for (int j = 1; j <= n; j++) {
				if ((a[p[i]][j] == 1) && (w[j - 1] == 0)) {
					go[i + 1][mask | (1 << (j - 1))] = true;
				}
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int mask = 0; mask < h; mask++) {
			vector <int> w = duo(mask, n);
			if (!go[i][mask]) continue;
			int cnt = 0;
			for (int j = 0; j < n; j++) {
				if ((a[p[i]][j + 1] == 1) && (w[j] == 0)) {
					cnt++;
				}
			}
			if (cnt == 0) return false;
		}
	}
	return true;
}

bool solve(int mask) {
	vector <int> w = duo(mask, n*n);
	int id = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			a[i][j] = w[id];
			id++;
		}
	}
	vector<int> p;
	for (int i = 0; i <n; i++) {
		p.push_back(i + 1);
	}
	bool ok = true;;
	do {
		if (!can(p)) {
			ok = false;
			break;
		}
	} while (next_permutation(p.begin(), p.end()));
	return ok;
}





int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int qq;
	cin >> qq;
	for (int qqq = 0; qqq < qq; qqq++)
	{
		cout << "Case #" << qqq + 1 << ": ";
		cin >> n;
		for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			cin >> s[i][j];
		int h = 1;
		for (int i = 0; i < n*n; i++)
			h *= 2;
		int ans = 2e9;
		for (int mask = 0; mask < h; mask++) {
			int flag = 0;
			int id = 0;
			vector <int> w = duo(mask, n*n);
			for (int i = 1; i <= n; i++)
			{
				for (int j = 1; j <= n; j++)
				{
					if (s[i][j] == '1' &&  w[id] == 0)
					{
						flag = -54545454;
					}
					if (s[i][j] == '0' && w[id] == 1)
					{
						flag++;
					}
					id++;
				}
			}
			if (flag < 0) continue;
			if (flag > ans) continue;
			if (solve(mask)) {
				ans = min(ans, flag);
			}
		}
		cout << ans << endl;


		/*double dp[205][205][205];
		for (int i = 0; i <= n; i++)
		for (int j = 0; j <= k; j++)
		for (int t = 0; t <= k; t++)
		dp[i][j][t] = .0;
		dp[0][0][0] = 1;
		for (int i = 1; i <= n; i++)
		for (int j = 0; j <= k; j++)
		for (int t = 0; t <= k/2; t++)
		{
		dp[i][j][t] = dp[i - 1][j][t];
		double cur = 0;
		for (int u = 1; u<i; u++)
		{
		double cur1 = 0;
		if (j>0)
		{
		cur1 += dp[u][j - 1][t] * (1 - p[i]);
		if (t > 0)
		cur1 += dp[u][j - 1][t - 1] * (p[i]);
		}
		cur = max(cur, cur1);
		}
		if (cur > dp[i][j][t])
		dp[i][j][t] = cur;
		}
		cout << setprecision(6)<<dp[n][k][k / 2] << endl;
		*/
	}
	return 0;
}