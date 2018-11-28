#if !ONLINE_JUDGE
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <stack>
using namespace std;

int main()
{
#if !ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output1.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++)
	{
		int maxi;
		string str;
		cin >> maxi;
		cin >> str;

		int count = 0;
		int ans = 0;
		for (int i = 0; i < str.length(); i++)
		{
			if (count < i)
			{
				ans += i - count;
				count = i;
			}
			count += str[i] - '0';
		}
		cout << "Case #"<<z<<": "<<ans << endl;
	}
	return 0;
}
