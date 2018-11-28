#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <list>

const std::vector<std::string> Words{ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

bool _GetDigits(const std::vector<unsigned int> Letters, const std::vector<unsigned int> Current, std::list<unsigned int> &Output)
{
	// Using all the letters
	if (Current == Letters)
		return true;

	for (unsigned int x = 0; x < Words.size(); x++)
	{
		unsigned int c = 0;
		for (c = 0; c < Words[x].size(); c++)
		{
			unsigned int Count = (unsigned int)std::count(Words[x].begin(), Words[x].end(), Words[x][c]);
			if (Letters[Words[x][c] - 'A'] < Count + Current[Words[x][c] - 'A'])
				break;
		}
		if (c == Words[x].size())
		{
			std::vector<unsigned int> NewDigits = Current;
			for (unsigned int y = 0; y < Words[x].size(); y++)
				NewDigits[Words[x][y] - 'A']++;

			if (_GetDigits(Letters, NewDigits, Output))
			{
				Output.push_front(x);
				return true;
			}
		}
	}

	return false;
}
std::list<unsigned int> GetDigits(const std::string Word)
{
	std::vector<unsigned int> Letters('Z' - 'A' + 1);
	for (unsigned int x = 0; x < Word.size(); x++)
		Letters[Word[x] - 'A']++;

	std::list<unsigned int> Out;
	std::vector<unsigned int> Current('Z' - 'A' + 1);

	if (_GetDigits(Letters, Current, Out))
		return Out;
	else
		throw std::exception();
}

int main(int argc, char *argv[])
{
	std::ifstream In("In.txt");
	std::ofstream Out("Out.txt");


	unsigned int T = 0;
	In >> T;

	for (unsigned int t = 0; t < T; t++)
	{
		std::string Word;
		In >> Word;

		std::list<unsigned int> Digits = GetDigits(Word);

		Out << "Case #" << t + 1 << ": ";
		for (std::list<unsigned int>::const_iterator i = Digits.cbegin(); i != Digits.cend(); i++)
			Out << *i;
		Out << std::endl;
	}

	In.close();
	Out.close();

	return 0;
}