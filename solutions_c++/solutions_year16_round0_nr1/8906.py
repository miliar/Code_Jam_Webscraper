// Test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <bitset>
using namespace std;


struct Item
{
	int carId;
	bool left;	
	int speed;
	int position;
};

void getDigits(unsigned long int n, bitset<10>& res)
{
	int mod;
	while (n > 0)
	{
		mod = n % 10;
		res[mod] = 1;
		n /= 10;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{	
	/*std::vector<Item> input;
	std::vector<std::vector<Item>> cases;*/

	unsigned long int input;
	std::vector<unsigned long int> cases;

	char *inname = "C:/Test/Debug/A-small.in";
    ifstream infile(inname);

	if (!infile) {
        cout << "There was a problem opening file "
             << inname
             << " for reading."
             << endl;
        return 0;
    }

	cout << "Opened " << inname << " for reading." << endl;

	int numCases;

    infile >> numCases;
    cout << "Num of cases is " << numCases << endl;
	
	for (int i=0; i<numCases; i++)
	{
		infile >> input;
		cases.push_back(input);
	}

	FILE * pFile;
    pFile = fopen ("out.txt","w+");

	for (int i=0; i<numCases; i++)
	{	
		input = cases[i];
		bitset<10> res;
		unsigned long int test=0;
		for (int j = 1; j < 100000; j++)
		{
			test = input * j;
			getDigits(test, res);
			if (res.all()) break;
		}
		if (res.all())
			fprintf(pFile, "Case #%d: %d\n", i + 1, test);
		else
			fprintf(pFile, "Case #%d: INSOMNIA\n", i + 1);
	}
	fclose (pFile);
	
	return 0;
}

