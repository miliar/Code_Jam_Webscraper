#include <bits/stdc++.h>
using namespace std;

int solve(const string &s)
{
	int sz = (int)s.size();
	int ans = 1;
	for (int i = 1; i < sz; i++)
	{
		if (s[i - 1] != s[i])
			ans++;
	}
	if (s[sz - 1] == '+')
		ans--;
	return ans;
}

int main()
{
	//freopen("xxx.in", "r", stdin);
	//freopen("xxx.out", "w", stdout);
	int T;
	cin >> T;
	string s;
	for (int i = 0; i < T; i++)
	{
		cin >> s;
		cout << "Case #" << i + 1 << ": " << solve(s) << "\n";	
	}
	return 0;
}