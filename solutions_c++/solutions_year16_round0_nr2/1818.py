#include <iostream>
#include <fstream>
#include <cstdio>
#include <climits>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <cmath>

using namespace std;

#define ll long long
#define vt vector
#define inf 1000000000
#define mod 1000000007

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tests = 1; tests <= t; tests++)
	{
		string s;
		cin >> s;
		int ans = 0;
		for (int i = 1; i < s.length(); i++)
		{
			if (s[i] != s[i - 1])
				ans++;
		}
		if (s[s.length() - 1] == '-')
			ans++;
		printf("Case #%d: %d\n", tests, ans);
	}
	return 0;
}