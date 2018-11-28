#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <functional>


using namespace std;

int NoLeft(int parties[], int P);
void foo(int parties[], int P, int C, ofstream& fout);

int main() {
	ofstream fout("output.txt");
	ifstream file;
	file.open("A-large.in", ios::in);    // open file

	int T;  // number of test cases
	file >> T;

	for (int i = 1; i <= T; i++)
	{
		int P;
		file >> P; // number of parties
		int parties[26];                  ////////////// change from 3 to 26

		for (int i = 0; i < P; i++)
		{
			file >> parties[i];
		}

		foo(parties, P, i, fout);

	}

	fout.close();
	file.close();
	return 0;
}

void foo(int parties[], int P, int C, ofstream& fout)
{
	fout << "Case #" << C << ":";
	while (NoLeft(parties, P) > 0)
	{
		int No = NoLeft(parties, P);
		char c;
		string out = "";
		int largestIndex = 0;
		for (int i = 1; i < P; i++)
		{
			if (parties[i] > parties[largestIndex])
				largestIndex = i;
		}
		parties[largestIndex]--;
		c = largestIndex + 65;
		out += c;

		//cout << "number of guys left: " << No << " , " << parties << endl;
		if (No != 3)
		{
			largestIndex = 0;
			for (int i = 1; i < P; i++)
			{
				if (parties[i] > parties[largestIndex])
					largestIndex = i;
			}
			parties[largestIndex]--;
			c = largestIndex + 65;
			out += c;
		}


		fout << " " << out;

	}

	fout << endl;

}

int NoLeft(int parties[], int P)
{
	int count = 0;
	for (int i = 0; i < P; i++)
	{
		count += parties[i];
	}
	return count;
}



