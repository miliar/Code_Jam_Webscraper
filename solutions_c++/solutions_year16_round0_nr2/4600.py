#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
	int t, x;
	cin.tie(0);
	ios::sync_with_stdio(false);
	cin >> t;
	for (x = 1; x <= t; ++x)
	{
		string s, t = "";
		cin >> s;
		int ans = 0, ans1 = 0, ans2 = 0;
		int flag = 0;
		t += s[0];
		for (int i = 1, j = 0; i < s.length(); ++i)
		{
			if (s[i] != t[j])
			{
				t += s[i];
				++j;
			}
		}
		if (t.size() == 1)
		{
			if (t[0] == '+')
				ans = 0;
			else
				ans = 1;
		}
		else {
			if (t[0] == '+')
			{
				if (t.size() % 2 == 0)
					ans = t.size();
				else
					ans = t.size() - 1;
			}
			else
			{

				if (t.size() % 2 == 0)
					ans = t.size() - 1;
				else
					ans = t.size();
			}
		}
		cout << "Case #" << x << ": " << ans << "\n";
	}
	return 0;
}