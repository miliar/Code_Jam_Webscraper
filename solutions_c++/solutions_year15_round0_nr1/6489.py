// gcj_a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>

using namespace std;

int ProcessTestCase(string& shynesslevels)
{
	int result = 0;
	int totalshyCount = 0;
	for (int counter = 0; counter < shynesslevels.length(); ++counter)
	{
		int shyCount = shynesslevels[counter] - '0';
		if (counter != 0 && totalshyCount + result < counter)
		{
			result += counter - totalshyCount - result;
		}
		totalshyCount += shyCount;
	}
	return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input("input.txt");
	ofstream output("output.txt");
	int N = 0;
	input >> N;
	for (int counter = 0; counter < N; ++counter)
	{
		int maxShyness = 0;
		input >> maxShyness;
		std::string shynesslevels = "";
		input >> shynesslevels;		
		output << "Case #" << counter+1 << ": " << ProcessTestCase(shynesslevels) << "\r\n";
	}	
	input.close();
	output.flush();
	output.close();
	return 0;
}

