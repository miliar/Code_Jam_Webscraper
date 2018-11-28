#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

int const Max = 111;

struct win
{
	string s;
	char let[Max];
	int num[Max];
	int k;
};

win str[Max];

int main()
{
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int test = 1; test <= t; test++)
	{
		int n;
		cin >> n;
		for (int i = 1; i <= n; i++)
		{
			cin >> str[i].s;
			str[i].k = 1;
			str[i].let[1] = str[i].s[0];
			str[i].num[1] = 1;
			for (int j = 1; j < str[i].s.length(); j++)
				if (str[i].s[j] == str[i].s[j - 1])
					str[i].num[str[i].k]++;
				else
				{
					str[i].k++;
					str[i].let[str[i].k] = str[i].s[j];
					str[i].num[str[i].k] = 1;
				}
		}
		bool err = false;
		for (int i = 2; i <= n; i++)
			if (str[i].k != str[1].k)
			{
				err = true;
				break;
			}
			else
			{
				for (int j = 1; j <= str[1].k; j++)
					if (str[i].let[j] != str[1].let[j])
					{
						err = true;
						break;
					}
				if (err)
					break;
			}
		cout << "Case #" << test << ": ";
		if (err)
			cout << "Fegla Won" << endl;
		else
		{
			int ans = 0;
			for (int j = 1; j <= str[1].k; j++)
			{
				int a[Max];
				for (int i = 1; i <= n; i++)
					a[i] = str[i].num[j];
				sort(a + 1, a + n + 1);
				int mid = a[n / 2 + 1];
				for (int i = 1; i <= n; i++)
					if (str[i].num[j] >= mid)
						ans += (str[i].num[j] - mid);
					else
						ans += (mid - str[i].num[j]);
			}
			cout << ans << endl;
		}
	}
	return 0;
}