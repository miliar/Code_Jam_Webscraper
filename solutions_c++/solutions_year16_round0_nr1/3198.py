#include <iostream>
#include <map>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int numberOfCases;
	ifstream in("A-large.in");
	ofstream out("output.txt");
	in >> numberOfCases;
	for (int i = 0; i < numberOfCases; i++)
	{
		int currentCase;
		in >> currentCase;
		if (currentCase == 0)
		{
			out << "Case #" << (i + 1) << ": INSOMNIA" << endl;
			continue;
		}
		map<int, bool> seenDigits;
		int currentNumber = 0;
		while (seenDigits.size() < 10)
		{
			currentNumber += currentCase;
			int temp = currentNumber;
			while (temp != 0)
			{
				seenDigits[temp % 10] = 1;
				temp /= 10;
			}
		}
		out << "Case #" << (i + 1) << ": " << currentNumber << endl;
	}

	return 0;
}