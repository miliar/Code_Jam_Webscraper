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





int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int qq;
	cin >> qq;
	for (int qqq = 0; qqq < qq; qqq++)
	{
		cout << "Case #" << qqq + 1 << ": ";
		int n, k;
		cin>>n>>k;
		vector <double> p(n);
		for (int i = 0; i < n; i++)
			cin >> p[i];
		sort(p.begin(), p.end());
		double dp[205][205][205];
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
	}
	return 0;
}