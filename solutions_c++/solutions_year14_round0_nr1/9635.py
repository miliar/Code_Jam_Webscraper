#include "stdafx.h"
#include <iostream>
using namespace std;
#pragma warning(disable:4996)

int sravn(int q1[4], int q2[4],int &m)
{
	int k = 0;
	for (int w = 0; w < 4; w++)
	{
		for (int e = 0; e < 4; e++)
		{
			if (q1[w] == q2[e]) { k++; m = q1[w]; }
		}
	}
	return k;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int exp, ch, mus[4], a1[4], a2[4], m = 0,chetexp = 1;
	cin >> exp;

	while (exp > 0)
	{
		cin >> ch;
		for (int i = 0; i < 4; i++)
		{
			if (ch == i + 1)
			{
				for (int j = 0; j < 4; j++)
				{
					cin >> a1[j];
				}
			}
			else
			{
				for (int j = 0; j < 4; j++)
				{
					cin >> mus[j];
				}
			}
		}

		cin >> ch;
		for (int i = 0; i < 4; i++)
		{
			if (ch == i + 1)
			{
				for (int j = 0; j < 4; j++)
				{
					cin >> a2[j];
				}
			}
			else
			{
				for (int j = 0; j < 4; j++)
				{
					cin >> mus[j];
				}
			}
		}

		cout << "Case #"<< chetexp<< ": ";
		switch (sravn(a1,a2,m))
		{
		case 0:
			cout << "Volunteer cheated!"<< endl;
			break;
		case 1:
			cout << m<< endl;
			break;
		default:
			cout << "Bad magician!" << endl;
			break;
		}
		chetexp++;
		exp--;
	}

	return 0;
}

