#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <ostream>

using std::string;

int main(int argc, char *argv[])
{
	int maxShy;
	string rep;
	int tests;

	std::fstream fs;
	fs.open(argv[1]);

	std::ofstream of;
	of.open("output.txt");

	std::string input;
	std::getline(fs, input);
	std::stringstream ss(input);

	ss >> tests;

	for (int j = 0; j < tests; j++)
	{
		std::string testcase;
		std::getline(fs, testcase);
		std::stringstream ss(testcase);

		ss >> maxShy >> rep;

		int sum = 0, nbOfInvites = 0;

		for (int i = 0; i <= maxShy; i++)
		{
			int diff = 0;
			if (sum < i)
			{
				diff = i - sum;
				nbOfInvites += diff;
				sum += diff;
			}
			sum += rep.at(i) - 48;
		}
		of << "Case #" << j + 1 << ": " << nbOfInvites << std::endl;
	}
}