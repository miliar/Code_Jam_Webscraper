#include <iostream>
#include <sstream>
#include <fstream>
#include <bitset>
#include <string>

using namespace std;

void checkDone(int number, std::bitset<10>& done)
{
	string numb = to_string(number);
	for (char c : numb)
	{
		int val = atoi(&c);
		done.set(val);
	}
}

int main()
{
	ifstream inputFile("A-large.in");
	ofstream outputFile("output.txt");

	int testNumber = 0;

	inputFile >> testNumber;



	for (int i = 1; i <= testNumber; ++i)
	{
		outputFile << "Case #" << i << ": ";
		int number, first;
		std::bitset<10> done(0);
		inputFile >> number;
		first = number;
		if (number == 0)
		{
			outputFile << "INSOMNIA" << endl;
			continue;
		}
		int multi = 2;
		while (true)
		{
			checkDone(number, done);
			if (done.all())
			{
				break;
			}
			number = first * multi;
			multi++;
		}

		outputFile << number << endl;
	}

	return 0;
}
