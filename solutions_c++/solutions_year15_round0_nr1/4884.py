#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int main()
{	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;	
	for (int tt = 1; tt <= t; tt++)
	{
		int n;
		cin >> n;
		string s;
		cin >> s;
		int have = 0, ans = 0;
		for (int j = 0; j < s.length(); j++)
		{
			int cur = s[j] - '0';
			if (cur != 0 && have < j)
			{
				ans += (j - have);
				have = j;
			}
			have += cur;
		}
		cout << "Case #" << tt << ": " << ans << endl;
	}
	cin >> t;
}