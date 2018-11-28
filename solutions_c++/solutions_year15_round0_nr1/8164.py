#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include <stdio.h>
#include<cstdlib>

using namespace std;

unsigned int tt, nn , needed , summ;

string stringayya;

//string filee[1] = {"t.txt"};


int main()
{
	freopen( "A-large.in" , "r" ,stdin ) ;

	freopen("ttt.txt", "w", stdout);

	cin >> tt;

	++tt;

	for (int itr = 1; itr < tt; ++itr)
	{
		summ = 0; needed = 0;

		cin >> nn >> stringayya;

		++nn;

		for (int itr2 = 0; itr2 < nn; ++itr2)
		{

			if (summ < itr2)
			{
				needed += itr2 - summ;

				summ = itr2;
			}

			summ += stringayya[itr2] - '0';
		}

		cout << "Case #" << itr << ": " << needed << endl;
	}

//	fclose(stdin);

	return 0;
}