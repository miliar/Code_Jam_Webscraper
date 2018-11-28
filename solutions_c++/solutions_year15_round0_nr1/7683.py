#include<iostream>
#include<fstream>
#include<string.h>
#include<stdio.h>
using namespace std;
#pragma warning (disable : 4996)

int main()
{
	int test, smax, b[5000], flag, temp, v, a[5000], q;
	char stringNumber[5000];
	freopen("inputa.txt", "r", stdin);
	freopen("outputa.txt", "w", stdout);


	cin >> test;

	for (q = 1; q <= test; q++)

	{

		temp = 0;
		v = 0;
		cin >> smax;
		//fflush(stdin);
		cin.clear();
		gets(stringNumber);
		for (int i = 1; i <= (strlen(stringNumber)-1); i++)
		{
			a[i] = stringNumber[i] - '0';
		}
		for (int i = 0; i <= smax; i++)
		{
			b[i] = 0;
			for (int j = i; j>0; j--)
			{
				if (i>0)
					b[i] = a[i - j+1] + b[i];

			}

			if ((b[i] + v) >= i)
			{

				flag = 0;

			}
			else
			{
				temp = temp + 1;
				v++;
			}
		}

		cout << "Case #" << (q) << ": " << (temp) << endl;

	}

	return 0;
}

