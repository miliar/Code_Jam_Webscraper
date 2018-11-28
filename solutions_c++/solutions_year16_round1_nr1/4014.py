// GoogleCodeJam_Round_1A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char findFirstLetterInWinningWord(string S);
string lastWord(string S);

int main() {
	int numTestCases;
	//ifstream infile("small_input.txt");
	ifstream infile("large_input.txt");
	infile >> numTestCases;
	int coutadjuster = 1;
	ofstream outfile("large_output.txt");
	for (int coutadjuster = 1; coutadjuster <= numTestCases; coutadjuster++)
	{
		string letters;
		infile >> letters;
		outfile << "Case #" << coutadjuster << ": " << lastWord(letters) << endl;
	}
	return 0;
}

string lastWord(string S)
{
	if (S.length() == 1)
	{
		return S;
	}
	string winningWord = { S[0] };
	for (int i = 1; i < S.length(); i++)
	{
		if (S[i] < winningWord[0])
		{
			winningWord += S[i];
		}
		else
		{
			winningWord = S[i] + winningWord;
		}
	}

	return winningWord;
}