#include<cstdio>
#include<iostream>
#include<string>
#pragma warning(disable : 4996)
using namespace std;

int main(void)
{
	freopen("C:\\Users\\user\\Desktop\\input.in", "r", stdin);
	freopen("C:\\Users\\user\\Desktop\\output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{

		string s;
		cin >> s;
		int k;
		cin >> k;
		int ans = 0;
		int len = s.length();

		//cout<<s<<" "<<k<<" "<<len<<endl;
		for (int j = 0; j < len; j++)
		{
			//cout << s << endl;
			if (j + k >len)
			{
				for (int g = j; g < len; g++)
				{
					if (s[g] != '+')
					{
						ans = -1;
						break;
					}
				}
			}
			else
			{
				if (s[j] == '+')
					continue;
				else
				{
					for (int g = j; g < j + k; g++)
					{
						if (s[g] == '-')
							s[g] = '+';
						else
							s[g] = '-';
					}
					ans++;
				}
			}
			if (ans < 0)
				break;
		}
		if (ans != -1)
			cout << "Case #" << i + 1 << ": " << ans << endl;
		else
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
	}
}
