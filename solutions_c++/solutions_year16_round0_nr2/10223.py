
#pragma warning(disable:4996)
//#include "stdafx.h"
//#include "CountingSheep.h"
#include <iostream>
#include <fstream>


using namespace std;

/* ID Pancakes */

void PankakesSmall()
{
	freopen("B-small-attempt4.in", "r", stdin);
	//freopen("mini.txt", "r", stdin);
	ofstream fout;
	fout.open("PancakeSmall.txt");
	int Test;

	cin >> Test;
	cin.ignore(); // remove line
	char stack[101];
	char input;
	int count[100];

	for (int t = 0; t < Test; t++)
	{
		for (int i = 0; i <= 100; i++)
			stack[i] = '+';

		//cin.ignore(); // remove line

		for (int i = 0; i < 100; i++)
		{
			input = cin.get();
			//cin.putback(input);
			if ((input != '+') && (input != '-'))
			{
				break;
			}
			else
				stack[i] = input;
		}
		//cin.ignore();
		//cout << "stack" << stack[0] << stack[1] << endl;

		count[t] = 0;
		for (int i = 0; i < 100; i++)
		{
			if (stack[i] != stack[i + 1])
				count[t]++;
		}
	
		

	}

	for (int t = 0; t < Test; t++)
	{ 
		fout << "Case #" << t + 1 << ": ";
		fout << count[t] << endl;
	}

	//fclose();
	
}

int main()
{
	PankakesSmall();
	int temp;
	cin >> temp;
	return 0;
}