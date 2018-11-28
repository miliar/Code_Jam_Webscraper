// ProblemA.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <numeric>


using namespace std;

unsigned long long solve(unsigned long long n) {

	bool digits[10];
	memset(digits, 0, 10);
	int count = 0;
	for (int i = 1; i < 1000; ++i)
	{
		unsigned long long nbr = n * i;
		for (;nbr > 0; nbr /= 10)
		{
			if (!digits[nbr % 10])
			{
				digits[nbr % 10] = true;
				++count;
				if (count == 10) {
					return n * i;
				}
			}
		}
	}
	return 0;
}

int main()
{
	fstream inFile("A-small-attempt0.in", ios::in);
	fstream outFile("A-small-attempt0.out", ios::out);
	int tests;
	inFile >> tests;
	for (int i = 0; i < tests; ++i)
	{
		int N;
		inFile >> N;
		
		unsigned long long ans = solve(N);
		outFile << "Case #" << (i + 1) << ": ";
		if (ans > 0)
			outFile << ans << endl;
		else
			outFile << "INSOMNIA" << endl;
	}
    return 0;
}

