#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int ans;
	int t;
	cin >> t;
	for (size_t i = 0; i < t; i++)
	{
		ans = 0;
		char data[105];
		cin >> data;
		cout << "Case #" << i + 1 << ": ";
		int lenth = strlen(data);
		data[lenth] = '+';
		data[lenth + 1] == '\0';
		for (int i = lenth-1; i >=0; i--)
		{
			if (data[i] != data[i + 1])
			{
				ans += 1;
			}
		}
		cout << ans << "\n";
	}
}