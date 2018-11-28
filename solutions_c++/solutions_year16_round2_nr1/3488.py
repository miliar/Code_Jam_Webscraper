#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <stack>
#include <sstream>
#include <algorithm>
#include <cmath>

template <typename T>
void printCase(int id, T result, std::stringstream& stream)
{
	stream << "Case #" << id + 1 << ": " << result << std::endl;
}

std::stringstream testResultStream;

std::string findNum(std::vector<int> wordCount, std::vector<std::string>& wordList, std::string current = "")
{
	bool finished = true;
	for (int i = 0; i < wordCount.size(); i++)
	{
		if (wordCount[i] > 0)
		{
			finished = false;
			break;
		}
	}

	if (finished)
		return current;

	for (int i = 0; i < wordList.size(); i++)
	{
		int foundIndex = i;
		for (int j = 0; j < wordList[i].size(); j++)
		{
			if (wordCount[wordList[i][j] - 'A'] == 0)
			{
				foundIndex = -1;
				break;
			}
		}

		if (foundIndex == -1)
			continue;

		std::vector<int> newWC(wordCount);
		for (int j = 0; j < wordList[i].size(); j++)
			newWC[wordList[i][j] - 'A']--;

		std::string newCurrent = current + std::to_string(i);

		std::string found = findNum(newWC, wordList, newCurrent);
		if (found != "")
			return found;
	}

	return "";
}

void computeTestCase(int id)
{
	std::string word;
	std::cin >> word;

	std::vector<int> count;
	count.resize(27);

	for (int i = 0; i < word.size(); i++)
		count[word[i] - 'A']++;

	std::vector<std::string> words;
	words.push_back("ZERO");
	words.push_back("ONE");
	words.push_back("TWO");
	words.push_back("THREE");
	words.push_back("FOUR");
	words.push_back("FIVE");
	words.push_back("SIX");
	words.push_back("SEVEN");
	words.push_back("EIGHT");
	words.push_back("NINE");

	std::string result = findNum(count, words);

	printCase(id, result, testResultStream);
}

int main()
{
	int T;
	std::cin >> T;

	std::string line;
	// Consume
	std::getline(std::cin, line);

	std::ofstream fStream;
	fStream.open("result.txt");

	for (int i = 0; i < T; i++)
		computeTestCase(i);

	fStream << testResultStream.str() << std::flush;
}