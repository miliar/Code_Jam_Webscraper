#include <fstream>
#include <iostream>
#include <string>

using namespace std;

bool hasNValue(const string &str, int n);
bool isVowel(char letter);

int main()
{
	ifstream fin("A-small.in");
	ofstream fout("A_small.out");

	int cases;
	fin >> cases;

	for (int index=0; index<cases; ++index)
	{
		string word;
		int n;
		fin >> word >> n;

		int count = 0;
		for (int i=0; i<word.size() - n + 1; ++i)
		{
			for (int j=n; j<word.size() - i + 1; ++j)
			{
				if (hasNValue(word.substr(i, j), n))
				{
					count += word.size() - i - j + 1;
					break;
				}
			}
		}

		fout << "Case #" << index + 1 << ": " << count << endl;
	}

	return 0;
}

bool hasNValue(const string &str, int n)
{
	int count = 0;
	for (int i=0; i<str.size(); ++i)
	{
		if (isVowel(str[i]))
			count = 0;
		else
		{
			if (++count == n)
				return true;
		}
	}
	return false;
}

bool isVowel(char letter)
{
	return letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u';
}