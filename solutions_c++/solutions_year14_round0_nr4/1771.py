// ConsoleApplication3.cpp : Defines the entry point for the console application.
//
// ConsoleApplication3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>

#include <algorithm>
using namespace std;




int _tmain(int argc, _TCHAR* argv[])
{
	int round;
	ifstream testfile("D-large.in");
	testfile >> round;
	ofstream outputfile("result.out");

	vector<float> Naomi, Ken;

	for (int i = 1; i <= round; i++)
	{
		int N;
		testfile >> N;
		Naomi.clear();
		Ken.clear();
		float temp;
		for (int j = 0; j < N; j++)
		{
			testfile >> temp;
			Naomi.push_back(temp);
		}

		for (int j = 0; j < N; j++)
		{
			testfile >> temp;
			Ken.push_back(temp);
		}

		std::sort(std::begin(Naomi), std::end(Naomi));
		std::sort(std::begin(Ken), std::end(Ken));

		int n = 0,  k= 0;
		int kenScore = 0;
		while (n < N && k < N)
		{
			if (Naomi[n] < Ken[k])
			{
				kenScore++;
				n++; k++;
			}
			else
			{
				k++;
			}
		}

		int normiScore = N - kenScore;

		n = 0; k = 0;
		kenScore = 0;
		while (n < N && k < N)
		{
			if (Naomi[n] > Ken[k])
			{
				n++;
				k++;
			}
			else
			{
				kenScore++;
				n++;
			}
			
		}

		int deceifulScore = N - kenScore;
		
		outputfile << "Case #" << i << ": " << deceifulScore << " " << normiScore << endl;
	}

	testfile.close();
	outputfile.close();

}




