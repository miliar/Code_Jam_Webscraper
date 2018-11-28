#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

inline int pow2roundup (int x)
{
	if (x < 0)
		return 0;
	--x;
	x |= x >> 1;
	x |= x >> 2;
	x |= x >> 4;
	x |= x >> 8;
	x |= x >> 16;
	return x+1;
}


int main() 
{ 
	int size = 0;
	std::ifstream in("A-large.in");

	int caseSize;
	in >> caseSize;

	std::ofstream out("Abig1out.txt", ios::out | ios::binary);

	for(int i = 0; i < caseSize; ++i)
	{
		int numberOfPeople;
		string ovation;
		in >> numberOfPeople >> ovation;
		
		int allStandingPeople = 0;
		int invitedPeople = 0;
		for(int j = 0; j < numberOfPeople + 1; ++j)
		{
			std::string::size_type sz;
			int currentNumber = ovation[j] - '0';

			if (allStandingPeople < j)
			{
				invitedPeople += j - allStandingPeople;
				allStandingPeople = j;
			}
			allStandingPeople += currentNumber;
		}


		out << "Case #" << i+1 <<": " << invitedPeople << "\n";
	}



	out.close();

	return 0; 
}