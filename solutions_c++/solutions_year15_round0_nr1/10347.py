#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<istream>
#include<ostream>
#include<fstream>
#include<stdio.h>

using namespace std;
int main()
{
	freopen("A-small-attempt5.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, x;
	cin >> T;
	string str;
	for (int j = 1; j <= T; j++)
	{
		cin >> x >> str;
		int counter = str[0] - 48, res = 0;
		for (int i = 1; i <= x; i++)
		{
			if (str[i] == '0')continue;
			if (counter >= i)
			{
				counter += (str[i] - 48);
			}
			else
			{
				res += (i - counter);
				counter += res + (str[i] - 48);
			}
		}
		cout << "Case #" << j << ": " << res << endl;

	}
}
