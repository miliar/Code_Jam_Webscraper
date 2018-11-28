#include <iostream>
#include <string>
#include <vector>

using namespace std;

// 1 = 1, i = 2, j = 3, k = 4
int grid[16] = {
	1, 2, 3, 4,
	2, -1, 4, -3,
	3, -4, -1, 2,
	4, 3, -2, -1
};

int multiply(int a, int b)
{
	bool aNeg = a != abs(a);
	bool bNeg = b != abs(b);

	int tempA = abs(a) - 1;
	int tempB = abs(b) - 1;
	int output = grid[tempB + tempA * 4];

	if (aNeg != bNeg)
	{
		output *= -1;
	}

	return output;
}

int characterToNum(char c)
{
	switch (c)
	{
	case '1':
		return 1;
		break;
	case 'i':
		return 2;
		break;
	case 'j':
		return 3;
		break;
	case 'k':
		return 4;
		break;
	}
}

bool findLetter(int letter, unsigned long long countStart, unsigned long long repetition, unsigned int character, string phrase)
{
	int finalChar = -1;
	if (countStart < repetition && character < phrase.size())
	{
		finalChar = characterToNum(phrase[character]);
		character += 1;
	}
	else if (countStart < repetition)
	{
		finalChar = characterToNum(phrase[0]);
		character = 1;
		countStart += 1;
	}
	for (unsigned long long count = countStart; count < repetition; count += 1, character = 0)
	{
		for (unsigned int nextCharacter = character; nextCharacter < phrase.size(); nextCharacter += 1)
		{
			if (finalChar == letter)
			{
				switch (letter)
				{
				case 2:
					return findLetter(3, count, repetition, nextCharacter, phrase);
					break;
				case 3:
					return findLetter(4, count, repetition, nextCharacter, phrase);
					break;
				case 4:
					finalChar = multiply(finalChar, characterToNum(phrase[nextCharacter]));
					break;
				}
			}
			else
			{
				finalChar = multiply(finalChar, characterToNum(phrase[nextCharacter]));
			}
		}
	}
	if (letter == 4 && finalChar == letter)
	{
		return true;
	}
	return false;
}
int main(int argc, char* argv[])
{
	unsigned int testCases = 0;
	cin >> testCases;

	vector<string> valid;

	for (unsigned int tc = 0; tc < testCases; tc += 1)
	{
		unsigned int characters;
		unsigned long long repetition;

		cin >> characters;
		string tempRep;
		cin >> tempRep;
		repetition = strtoull(tempRep.c_str(), 0, 10);

		string phrase;
		cin >> phrase;

		if (findLetter(2, 0, repetition, 0, phrase))
		{
			valid.push_back("YES");
		}
		else
		{
			valid.push_back("NO");
		}
	}

	for (unsigned int tc = 0; tc < testCases; tc += 1)
	{
		cout << "Case #" << tc + 1 << ": " << valid[tc] << endl;
	}
}

