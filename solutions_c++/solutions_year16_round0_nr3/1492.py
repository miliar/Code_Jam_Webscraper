// 2016QualificationRound.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <bitset>

using namespace std;

const int N = 32;
const int J = 500;

const size_t MarkerSize = N / 2 - 1;

using Marker = bitset<MarkerSize>;

string Make(const Marker& m)
{
	stringstream ss;
	ss << "1";

	for (int i = 0; i < MarkerSize; i++)
	{
		if (m[i])
			ss << "11";
		else
			ss << "00";
	}

	ss << "1";
	return ss.str();
}

int main()
{
	unsigned long seed = 0;

	cout << "Case #1:" << endl;

	for (size_t i = 0; i < J; i++)
	{
		cout << Make(seed++) << " 3 4 5 6 7 8 9 10 11" << endl;
	}

	return 0;
}

