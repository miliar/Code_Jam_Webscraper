#include "stdafx.h"
//#include "CountingSheep.h"
#include <iostream>
#include <fstream>

using namespace std;

/* ID BOARDCOVER */
bool result[10];
int  IsTen = 0;
int  modular = 1;
void RunCountingSheep()
{
	freopen("A-small-attempt1.in", "r", stdin);
	
	ofstream fout;
	fout.open("OutputCountingSheep.txt");
	int Test;

	cin >> Test;

	int N;
	int temp;
	for (int t = 0; t < Test; t++)
	{
		for (int i = 0; i < 10; i++)
			result[i] = false;

		cin >> N;
		IsTen = 0;
		fout << "Case #" << t + 1 << ": ";
		for (int i = 1; i < 100; i++)
		{
			temp = N * i;
			int index = 0;
			//modular = 1;
			for (int j = 1; j < 10; j++)
			{
				index = temp % 10;
				result[index] = true;
				//cout << index << " ";
				temp = temp / 10;
				if (temp == 0)
					break;
			}

			for (int j = 0; j < 10; j++)
				IsTen = IsTen + result[j];

			if (IsTen == 10)
			{
				//cout << endl;
				fout << N * i << endl;
				break;
			}
			IsTen = 0;

			if (i == 99)
			{
				fout << "INSOMNIA" << endl;
			}
		}
	}
	//fclose();
	
}

int main()
{
	RunCountingSheep();
	int temp;
	cin >> temp;
	 return 0;
}