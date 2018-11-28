#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <deque>

using namespace std;

int sgn(int val) {
	return (0 < val) - (val < 0);
}

int symbolToindex(int c)
{
	if(c == 1)
		return 0;
	if (c == 'i')
		return 1;
	if (c == 'j')
		return 2;
	if (c == 'k')
		return 3;

	return -1;
}		


int q_multiply(int c1, int c2)
{
	int sign = sgn(c1) * sgn(c2); 
	c1 = std::abs(c1);
	c2 = std::abs(c2);

	int table[4][4] = {
		{1,   'i', 'j', 'k'},
		{'i', -1, 'k', -'j'},
		{'j', -'k', -1, 'i'},
		{'k', 'j', -'i', -1},
	};
	
	return sign * table[symbolToindex(c1)][symbolToindex(c2)];	
}


int main() 
{ 
	int size = 0;
	std::ifstream in("C-small-attempt0.in");

	int caseSize;
	in >> caseSize;

	std::ofstream out("C1_small.txt", ios::out | ios::binary);

	for(int i = 0; i < caseSize; ++i)
	{
		int numberOfLetters;
		int multiply;
		string str;
		in >> numberOfLetters >> multiply >> str;

		const int DIJKSTRA_STRING[3] = {'i', 'j', 'k'};

		int globalChar = 1;
		int passingIndex = 0;
		for(int i = 0; i < numberOfLetters * multiply; ++i)
		{
			int realIndex = i % numberOfLetters;
			int currentChar =  str[realIndex];

			globalChar = q_multiply(globalChar, currentChar);

			if (passingIndex > 2)
			{
				continue;
			}

			if (globalChar == DIJKSTRA_STRING[passingIndex])
			{
				globalChar = 1;
				passingIndex++;
			}
		}

		const char* unswer = (passingIndex == 3 && globalChar == 1) ? "YES" : "NO";
		out << "Case #" << i+1 <<": " << unswer << "\n";
	}



	out.close();

	return 0; 
}