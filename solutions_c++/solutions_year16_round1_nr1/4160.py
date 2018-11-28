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
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tests = 1; tests <= t; tests++)
	{
		string s;
		cin >> s;
		string ans = "";
		for (int i = 0; i < s.length(); i++)
		{
			if (ans == "")
				ans += s[i];
			else
			{
				if (ans[0] > s[i])
					ans += s[i];
				else
					ans = s[i] + ans;
			}
		}
		printf("Case #%d: %s\n", tests,ans.c_str());
	}
	return 0;
}