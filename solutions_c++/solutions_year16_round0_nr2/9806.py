#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int main()
{
	ifstream fin("file.in");
	ofstream fout("file.out");

	int CASES;
	fin >> CASES;
	for (int CASE = 1; CASE <= CASES; CASE++)
	{
		string asdf;
		fin >> asdf;
		
		int counter = 1;
		char currentchar = asdf[0];
		for (int i = 1; i < asdf.length(); i++)
		{
			if (asdf[i] != currentchar)
			{
				counter++;
				currentchar = asdf[i];
			}
		}
		if (asdf[asdf.length() - 1] == '+')
		{
			counter--;
		}
		
		fout << "Case #" << CASE << ": " << counter << endl;
		
	}

}