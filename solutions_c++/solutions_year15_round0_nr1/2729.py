#include <iostream>
#include <fstream>

#define READFROMFILE
#define WRITETOFILE

int main()
{
	int numOfTestCases;

#ifdef READFROMFILE
	std::ifstream input("ProblemAIn.txt", std::ifstream::in);
#else
	std::istream &input = std::cin;
#endif

#ifdef WRITETOFILE
	std::ofstream output("ProblemAOut.txt", std::ofstream::out);
#else
	std::ostream &output = std::cout;
#endif

	input >> numOfTestCases;

	for (int testCase = 1; testCase <= numOfTestCases; testCase++)
	{
		int sMax;
		int standingCount = 0;
		int friendsNeeded = 0;

		input >> sMax;

		for (int i = 0; i <= sMax; i++)
		{
			char num;

			input >> num;
			int people = num - '0';
			if (standingCount >= i)
				standingCount += people;
			else
			{
				int friends = i - standingCount;
				friendsNeeded += friends;
				standingCount += people + friends;
			}
		}

		output << "Case #" << testCase << ": " << friendsNeeded << std::endl;
	}
}