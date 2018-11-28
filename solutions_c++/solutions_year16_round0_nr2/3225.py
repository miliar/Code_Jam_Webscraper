#include <iostream>
#include <sstream>
#include <fstream>
#include <bitset>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<bool> transfome(const string& sequence)
{
	std::vector<bool> res(sequence.size(), false);
	int i = 0;
	for (const char& c : sequence)
	{
		if (c == '+')
		{
			res[i] = true;
		}
		++i;
	}
	reverse(res.begin(), res.end());

	return res;
}

void flip(vector<bool>& vec, int from)
{
	for (unsigned int i = from; i < vec.size(); ++i)
	{
		vec[i].flip();
	}
}

int main()
{
	ifstream inputFile("B-large.in");
	ofstream outputFile("output.txt");

	int testNumber = 0;

	inputFile >> testNumber;

	for (int i = 1; i <= testNumber; ++i)
	{
		outputFile << "Case #" << i << ": ";
		std::string sequence;

		inputFile >> sequence; 
		int cpt = 0;
		std::vector<bool> seq = transfome(sequence);
		for (unsigned int i = 0; i < seq.size(); ++i)
		{
			if (!seq[i])
			{
				flip(seq, i);
				cpt++;
			}
		}
		outputFile << cpt << endl;
	}

	return 0;
}
