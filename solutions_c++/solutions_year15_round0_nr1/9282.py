#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
using namespace std;

int main()
{
#ifndef __OLIMP__
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T = 0;
	int TC;
	int res;
	int acum;
	int S;
	string audience;
	cin >> TC;
	while (T++ < TC)
	{
		cin >> S;
		cin >> audience;
		res = 0;
		acum = audience[0] - '0';
		for (int i = 1; i <= S; i++)
		{
			int numOfType = audience[i] - '0';
			if (acum < i)
			{
				res += i - acum;
				acum += i - acum;
			}

			acum += numOfType;
		}

		cout << "Case #" << T << ": " << res << endl;
	}
}
