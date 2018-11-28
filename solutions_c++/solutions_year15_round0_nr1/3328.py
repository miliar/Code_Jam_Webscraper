#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int n;
		cin >> n;
		string str;
		cin >> str;
		int cur_up = 0;
		int ans = 0;
		for (int j = 0; j <= n; j++)
		{
			int cur_num = str[j] - '0';
			if (j > cur_up)
			{
				int del = -cur_up + j;
				ans += del;
				cur_up += del;
			}
			cur_up += cur_num;
		}
		printf("Case #%d: %d\n", i, ans);
	}
	//for (;;);
	return 0;
}