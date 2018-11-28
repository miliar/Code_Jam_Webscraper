#include <iostream>
#include <stdio.h>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
	freopen("src.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tt;
	cin >> tt;
	for (int t = 1; t <= tt;t++)
	{
		int freq[10001] = { 0 };
		int l;
		string s;
		cin >> l >> s;
		freq[0] = s[0] - '0';
		for (int i = 1; i < s.size(); i++)
			freq[i] = freq[i - 1] + (s[i] - '0');
		int cnt = 0;
		for (int i = 1; i < s.size(); i++)
		{
			if (i > freq[i - 1])
			{
				int val = i - freq[i - 1];
				cnt += val;
				for (int j = i; j < s.size(); j++)
					freq[j] += val;
			}
		}
		cout << "Case #" << t << ": " << cnt << endl;
	}
	return 0;
}