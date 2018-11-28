#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::ifstream In;
std::ofstream Out;

class LetterPair
{
public:
	char Letter;
	unsigned int Repeats;

	LetterPair(const char Letter)
		:Letter(Letter),
		Repeats(1)
	{
	}
};

std::vector<LetterPair> CreatePairs(const std::string Input)
{
	std::vector<LetterPair> Pairs;
	Pairs.push_back(LetterPair(Input[0]));

	for (unsigned int x = 1; x < Input.size(); x++)
	{
		if (Pairs[Pairs.size() - 1].Letter == Input[x])
		{
			Pairs[Pairs.size() - 1].Repeats++;
		}
		else
		{
			Pairs.push_back(LetterPair(Input[x]));
		}
	}

	return Pairs;
}

void Print(const int Result, const unsigned int Case)
{
	Out << "Case #" << (Case + 1) << ": ";
	if (Result == -1)
	{
		Out << "Fegla Won";
	}
	else
	{
		Out << Result;
	}
	Out << std::endl;
}

int main(int argc, char *argv[])
{
	In.open("In.txt");
	Out.open("Out.txt");

	unsigned int TestCases = 0;
	In >> TestCases;

	for (unsigned int x = 0; x < TestCases; x++)
	{
		unsigned int N = 0;
		In >> N;
		std::vector<std::vector<LetterPair>> Pairs;

		for (unsigned int y = 0; y < N; y++)
		{
			std::string Temp;
			In >> Temp;
			Pairs.push_back(CreatePairs(Temp));
		}

		// Check if possible
		bool Possible = true;
		for (unsigned int y = 1; y < Pairs.size(); y++)
		{
			if (Pairs[0].size() != Pairs[y].size())
			{
				Possible = false;
				break;
			}
			for (unsigned int z = 0; z < Pairs[0].size(); z++)
			{
				if (Pairs[0][z].Letter != Pairs[y][z].Letter)
				{
					Possible = false;
					break;
				}
			}
			if (!Possible)
			{
				break;
			}
		}
		if (!Possible)
		{
			Print(-1, x); // Impossible - one word has a different set of letters
			continue; // Next test case
		}

		unsigned int Operations = 0;

		for (unsigned int y = 0; y < Pairs[0].size(); y++)
		{
			// Find average value (requires fewest operations to reach)
			unsigned int Average = 0;
			for (unsigned int z = 0; z < Pairs.size(); z++)
			{
				Average += Pairs[z][y].Repeats;
			}
			Average = (unsigned int)round((double)Average / (double)Pairs.size()); // Average repeats per letter
			
			for (unsigned int z = 0; z < Pairs.size(); z++) // Need as many operations on this letter as there are differences
			{
				Operations += abs((int)Average - (int)Pairs[z][y].Repeats);
			}
		}

		Print(Operations, x);
	}

	In.close();
	Out.close();

	return 0;
}