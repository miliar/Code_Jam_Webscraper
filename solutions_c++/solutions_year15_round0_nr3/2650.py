#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

vector<vector<int>> table
{
	{ 1, 2, 3, 4 },
	{ 2, -1, 4, -3 },
	{ 3, -4, -1, 2 },
	{ 4, 3, -2, -1 }
};

int mult(int a, int b)
{
	if (a == 1) return b;
	if (b == 1) return a;
	int nega = 1, negb = 1;

	if (a < 0)
	{
		nega *= -1;
		a *= -1;
	}
	if (b < 0)
	{
		negb *= -1;
		b *= -1;
	}

	int r = table[a - 1][b - 1];
	return r * nega * negb;
}

int toint(char x)
{
	switch (x)
	{
	case 'i': return 2;
	case 'j': return 3;
	case 'k': return 4;
	}

	return 0;
}

int main()
{
	ifstream in("in.txt");
//	cin.rdbuf(in.rdbuf());

	int t;
	cin >> t;

	//for (int i = 1; i <= 4; i++)
	//{
	//	for (int j = 1; j <= 4; j++)
	//	{
	//		cout << mult(-i, -j) << ' ';
	//	}
	//	cout << endl;
	//}

	//cout << mult(toint('j'), toint('i')) << endl;
//	cout << mult(mult(toint('j'), toint('i')), toint('j')) << endl;

	for (int tc = 1; tc <= t; tc++)
	{
		int L, X;
		cin >> L >> X;

		string data;
		cin >> data;

		bool yes = false;
		unsigned long long p1 = 0;

		int reduce1 = 1;
		int x = p1 / L;
		bool firstrun = true;

		for (; !yes && x < X;)
		{
			for (; (firstrun || reduce1 != 2) && x < X;)
			{
				unsigned long long ip1 = p1 % L;

				firstrun = false;
				reduce1 = mult(reduce1, toint(data[ip1]));
				p1++;

				if ((p1 % L) == 0)
				{
					x++;
				}
			}

			p1--;
			unsigned long long p2 = p1 + 1;
			int reduce2 = 1;

			for (; reduce2 != 3 && x < X;)
			{
				unsigned long long ip2 = p2 % L;

				reduce2 = mult(reduce2, toint(data[ip2]));
				p2++;

				if ((p2 % L) == 0)
				{
					x++;
				}
			}

			p2--;
			int reduce3 = 1;

			for (unsigned long long p3 = p2 + 1; x < X;)
			{
				unsigned long long ip3 = p3 % L;

				reduce3 = mult(reduce3, toint(data[ip3]));
				p3++;

				if ((p3 % L) == 0)
				{
					x++;
				}
			}

			yes = (reduce1 == 2 && reduce2 == 3 && reduce3 == 4);
			p1++;
			x = p1 / L;
			firstrun = true;
		}

		cout << "Case #" << tc << ": " << (yes ? "YES":"NO") << endl;
	}

	return 0;
}
