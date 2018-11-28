#include <iostream>
#include <sstream>
#include <fstream>
#include <bitset>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>
#include <map>

using namespace std;

int main()
{
	ifstream inputFile("A-large(1).in");
	ofstream outputFile("output.txt");

	int testNumber = 0;

	inputFile >> testNumber;
	std::map<int, std::string> numbers;

	numbers[0] = "ZERO";
	numbers[1] = "ONE";
	numbers[2] = "TWO";
	numbers[3] = "THREE";
	numbers[4] = "FOUR";
	numbers[5] = "FIVE";
	numbers[6] = "SIX";
	numbers[7] = "SEVEN";
	numbers[8] = "EIGHT";
	numbers[9] = "NINE";

	std::unordered_map<char, int> unique;
	unique['Z'] = 0;
	unique['W'] = 2;
	unique['X'] = 6;
	unique['G'] = 8;
	unique['U'] = 4;
	unique['F'] = 5;
	unique['S'] = 7;
	unique['I'] = 9;
	unique['T'] = 3;

	std::string sentenceUnique = "ZWXGUFSIT";

	for (int i = 1; i <= testNumber; ++i)
	{
		outputFile << "Case #" << i << ": ";
		std::string sentence;

		inputFile >> sentence;
		std::vector<int> solution;
		
		/// search only digit
		for (auto& g : sentenceUnique)
		{
			int number = std::count(sentence.begin(), sentence.end(), g);
			for (int k = 0; k < number; ++k)
			{
				solution.push_back(unique[g]);
			}

			for (int l = 0; l < number; ++l)
			{
				// remove one of each
				for (char c : numbers[unique[g]])
				{
					auto it = std::find(sentence.begin(), sentence.end(), c);
					sentence.erase(it);
				}
			}
		}

		int numberOfOne = sentence.size() / 3;
		for (int k = 0; k < numberOfOne; ++k)
		{
			solution.push_back(1);
		}
		std::sort(solution.begin(), solution.end());

		for (int i : solution)
		{
			outputFile << i;
		}

		outputFile << endl;
	}

	return 0;
}
