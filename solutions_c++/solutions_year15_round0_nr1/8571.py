#include <iostream>
#include <iomanip>
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

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		int n;
		string s;
		cin >> n >> s;
		int cnt = 0, ans = 0;
		for (int i = 0; i <= n; i++)
		{ 
			if (cnt < i && s[i] > '0')
			{
				ans += i - cnt;
				cnt += i - cnt;
				cnt += s[i] - '0';
			}
			else
				cnt += s[i] - '0';
		}
		cout << "Case #" << cases << ": " << ans << '\n';
	}
	return 0;
}