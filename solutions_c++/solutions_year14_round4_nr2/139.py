#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
using namespace std;
int n, a[1009];
int ans;
int init()
{
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> a[i];
	return 0;
}

int work()
{
	ans = 0;
	int left = 0;
	int right = n - 1;
	for (int i = 0; i < n - 1; i++)
	{
		int k = left;
		for (int j = left; j <= right; j++)
		if (a[j] < a[k])
			k = j;
		if (k - left < right - k)
		{
			ans += k - left;
			for (int j = k; j > left; j--)
				swap(a[j], a[j - 1]);
			left++;
		}
		else
		{
			ans += right - k;
			for (int j = k; j < right; j++)
				swap(a[j], a[j + 1]);
			right--;
		}
	}
	return 0;
}

int main()
{
	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		init();
		work();
		cout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}