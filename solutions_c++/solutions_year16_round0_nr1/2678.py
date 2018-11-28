#include <iostream>
#include <algorithm>
using namespace std;

void printSolution(unsigned int T, unsigned int solution)
{
	cout << "Case #" << T << ": ";
	if (solution == 0)
		cout << "INSOMNIA" << endl;
	else
		cout << solution << endl;
}

unsigned int seenIn( unsigned int number)
{
	unsigned int seen = 0;
	while (number > 0)
	{
		seen |= 1 << (number % 10);
		number /= 10;
	}

	return seen;
}

void solve(unsigned int T)
{
	unsigned int N;
	cin >> N;
	unsigned int cN = N;

	if (N > 0) 
	{
		unsigned int alreadySeen = 0;

		while (true)
		{
			alreadySeen |= seenIn(cN);
			if (alreadySeen == 1023)
				break;
			cN += N;
		}
	}

	printSolution(T,cN);
}

int main( int argc, char** argv )
{
	int T;
	cin >> T;

	for ( int i = 1; i <= T; ++i ) solve(i);
	return 0;
}
