// EoPI.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <algorithm>
#include <fstream>
#include <iostream>
#include <ostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>


using namespace std;


int getNum(string str)
{
	if (stoi(str) == 0) return 0;

	int x = 0x0000;
	int N = stoi(str);

	if (N < 0) N *= -1;

	int i = 1;
	while (x != 1023)
	{
		int crntNum = N * i;

		for (int exp = 1; crntNum / exp > 0; exp *= 10)
		{
			x |= 1 << ((crntNum / exp) % 10);
		}

		if (x == 1023) return crntNum;

		i++;
	}
}



int main()
{

	ifstream inFile;
	inFile.open("C:\\Temp\\GoogleCodeJam\\A-large.in");

	ofstream outFile;
	outFile.open("C:\\Temp\\GoogleCodeJam\\outPut.txt");

	string line;
	getline(inFile, line);
	int numCases = stoi(line);

	int CaseNum = 1;
	while (numCases > 0)
	{
		getline(inFile, line);
		string N = line;

		int Num = getNum(N);

		if(Num == 0)
			outFile << "Case #"<< CaseNum++ << ":"<< " " <<"INSOMNIA"<<endl;
		else
			outFile << "Case #"<< CaseNum++ << ":"<< " " << Num<<endl;

		numCases--;
	}
	inFile.close();
	outFile.close();



	system("pause");
	return 0;
}

