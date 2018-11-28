#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <map>
#include <limits>
#include <set>

using namespace std;

map <long long int, long long int> mp;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		string s;
		cin >> s;
		char oct = s[0];
		int ans = 0;
		for (int j = 0; j < s.length(); j++)
		{
			while (j + 1 < s.length() && s[j] == s[j + 1])
				j++;
			if (s[j] != oct)
			{
				oct = s[j];
				ans++;
			}	
		}
		if (oct == '-')
			ans++;
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
}