#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cout << "Case #" << tt << ": ";
		string s;
		cin >> s;
		s += "+";
		int ans = 0;
		for (int i = 1; i < s.length(); i++)
			ans += s[i] != s[i - 1];
		cout << ans << endl;
	}
}