#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		int k;
		string s;
		cin >> k >> s;
		int cur = 0;
		int ans = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (cur < i)
			{
				ans += i - cur;
				cur = i + s[i] - '0';
			}
			else
			{
				cur += s[i] - '0';
			}
		}
		cout << "Case #" << i << ": " << ans << endl;
	}

}
