#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

void printSolution(unsigned int T, unsigned int flips)
{
	cout << "Case #" << T << ": " << flips << endl;
}


void solve(unsigned int T)
{
	string pancakeStackString;
	cin >> pancakeStackString;
	// vector<bool> pancakeStack(pancakeStackString.length());

	// Initialize the pancakeStack
	// for (size_t i = 0; i < pancakeStackString.length(); ++i)
		// pancakeStack.at(i) = pancakeStackString.at(i) == '+';

	int index = pancakeStackString.length()-1;
	unsigned int flips = 0;
	char type = '+';
	while (index >= 0)
	{
		if (pancakeStackString.at(index)!=type)
		{
			type = pancakeStackString.at(index);
			++flips;
		}
		--index;
	}

	
	printSolution(T,flips);
}

int main( int argc, char** argv )
{
	int T;
	cin >> T;

	for ( int i = 1; i <= T; ++i ) solve(i);
	return 0;
}
