#include <stdlib.h>
#include <string>
#include <assert.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>
#include <sstream>

using namespace std;

string shift(string word, char c)
{
	string s;
	s += c;

	for (int i = 0; i < word.size(); i++)
	{
		s += word[i];
	}

	return s;
}

int main()
{
	int testCases;
	cin >> testCases;

	cin.ignore(10000, '\n');

	for (int i = 1; i <= testCases; i++)
	{
		string S;

		getline(cin, S);

		int size = S.size();

		string lastWord;
		lastWord += S[0];
		int lastSize = 1;

		for (int j = 1; j < size; j++)
		{
			if (lastWord[0] > S[j])
				lastWord += S[j];
			else
				lastWord = shift(lastWord, S[j]);
		}

		cout << "Case #" << i << ": " << lastWord << endl;
	}
}