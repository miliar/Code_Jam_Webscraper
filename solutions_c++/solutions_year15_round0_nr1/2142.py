#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<cstdio>

using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	int k;
	int a;
	int m,p;
	string s;
	cin >> k;
	for (int i = 1; i <= k; i++)
	{
		m = 0;
		p = 0;
		cin >> n;
		cin >> s;
		for (int j = 0; j <= n; j++)
		{
			a = int(s[j]) - int('0');
			if (a != 0)
			{
				if (m >= j)
				{
					m += a;
				}
				else
				{
					p += j - m;
					m = j + a;
				}
			}
		}
		cout << "Case #" << i << ": " << p << endl;;
	}
	return 0;
}
