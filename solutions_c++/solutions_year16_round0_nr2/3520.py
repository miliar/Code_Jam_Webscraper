/*
Problem #524 Prime Ring Problem - UVA
http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=465
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <bitset>
using namespace std;

typedef long long ll;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	
	int t;
	int ans;
	string s;
	cin >> t;
	for (int z = 1; z <= t; z++)
	{
		cin >> s;
		ans = 0;
		for (int i = 1; i < s.length(); i++)
			if (s[i] != s[i - 1])
				ans++;

		if (s.back() == '-')
			ans++;

		printf("Case #%d: %d\n", z, ans);
	}
	return 0;
}
