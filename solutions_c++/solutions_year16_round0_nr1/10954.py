#include<iostream>
#include<string>

using namespace std;

int main()
{
	int i;
	int j;
	int n;
	freopen("E:\\WorkShop\\CodeJam2016\\A-large.in", "r", stdin);
	freopen("E:\\WorkShop\\CodeJam2016\\outlarge.txt", "w", stdout);
	char rec[500];
	int testcase = 1, test;
	cin >> test;
	for (testcase = 1; testcase <= test;testcase++)
	{
		cin >> n;
		int backup = n;
		cout << "Case #" << testcase << ": ";
		for (i = '0'; i <= '9'; i++)
		{
			rec[i] = 0;
		}

		for (i = 1; i < 1000;i++)
		{
			n = backup*i;
			string s = to_string(n);
			for (j = 0; j < s.length(); j++)
			{
				rec[s[j]]++;
			}
			bool flag = true;

			for (j = '0'; j <= '9'; j++)
			{
				if (rec[j] == 0)
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
		}// 1000 loop ended
		if (i == 1000)
		{
			cout << "INSOMNIA" << endl;
		}
	}// input ended
	return 0;
}