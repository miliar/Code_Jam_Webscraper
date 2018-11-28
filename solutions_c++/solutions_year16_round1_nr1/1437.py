#include <iostream>
#include <cstring>
#include <string>

using namespace std;

string s, ans;

void calc()
{
	ans = "";
	int len = s.length();
	ans += s[0];
	for (int i = 1; i < len; i++)
	{
		if (s[i] >= ans[0])
			ans = s[i] + ans;
		else
			ans = ans + s[i];
	}
	cout << ans << endl;
	return;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out-2.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		s = "";
		cin >> s;
		cout << "Case #" << i << ": ";
		calc();
	}
	return 0;
}