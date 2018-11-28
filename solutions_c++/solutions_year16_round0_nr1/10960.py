#include<iostream>
#include<string>

using namespace std;

int main()
{
	int i;
	int j;
	int n;
	freopen("E:\\WorkShop\\CodeJam2016\\A-large.in", "r", stdin);
	freopen("E:\\WorkShop\\CodeJam2016\\large.txt", "w", stdout);
	char track[1000];
	int t = 1, test;
	cin >> test;
	for (t = 1; t <= test;t++)
	{
		cin >> n;
		int backup = n;
		cout << "Case #" << t << ": ";
		for (i = '0'; i <= '9'; i++)
			track[i] = 0;

		for (i = 1; i < 1000;i++)
		{
			n = backup*i;
			string s = to_string(n);
			for (j = 0; j < s.length(); j++)
			{
				track[s[j]]++;
			}
			bool flag = true;

			for (j = '0'; j <= '9'; j++)
			{
				if (track[j] == 0)
				{
					flag = false; break;
				}
			}
			if (flag)
			{
				cout << n << endl;
				break;
			}
			if (n == backup && i != 1)
			{
				i = 1000;
				break;
			}
		}
		if (i == 1000)
		{
			cout << "INSOMNIA" << endl;
		}
	}
	return 0;
}