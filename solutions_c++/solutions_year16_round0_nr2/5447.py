//be naame khodaa

#include <bits/stdc++.h>

using namespace std;

bool mark[10];

int main()
{
	int n, t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		string s;
		cin >> s;
		int ans = 1;
		for (int i = 1; i < s.length(); i++)
			if (s[i] != s[i-1])
				ans++;
		int len = s.length();
		if (s[len-1] == '+') ans--;
		printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}
