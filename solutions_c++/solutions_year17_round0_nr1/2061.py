#include<cstdio>
#include<iostream>
#include<string>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		string s;
		int k;
		cin >> s >> k;
		cout << "Case #" << (q + 1) << ": ";
		int len = (int)s.length();
		int cnt = 0;
		int flag = 1;
		for (int i = 0; i < len; i++)
			if (s[i] == '-')
			{
				if (i <= len - k)
				{
					cnt++;
					for (int j = i; j < i + k; j++)
						if (s[j] == '-')
							s[j] = '+';
						else
							s[j] = '-';
				}
				else
				{
					cout << "IMPOSSIBLE\n";
					flag = 0;
					break;
				}
			}
		if (flag)
			cout << cnt << "\n";
	}
	return 0;
}