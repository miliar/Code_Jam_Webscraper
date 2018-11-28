#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
#pragma warning(disable:4996)

typedef unsigned int uint;

string genarateLastWord(const string& str)
{
	string lastWord = "";
	lastWord.append(str, 0, 1);
	for (uint i = 1; i < str.size(); ++i)
	{
		int valLastWordLetter = lastWord[0];
		int valSLetter = str[i];

		if (valLastWordLetter <= valSLetter)
		{
			lastWord.insert(lastWord.begin(), 1, str[i]);
		}
		else
		{
			lastWord.insert(lastWord.end(), 1, str[i]);
		}
	}
	return lastWord;
}

int main()
{
	freopen("C:\\Users\\Dilum\\Desktop\\SingaJob\\GoogleCodeJam_2016\\Debug\\input.in", "r", stdin);
	freopen("C:\\Users\\Dilum\\Desktop\\SingaJob\\GoogleCodeJam_2016\\Debug\\output.txt", "w", stdout);

	size_t testCases;
	cin >> testCases;
	size_t caseNumber = 1;

	while (caseNumber <= testCases)
	{
		cout << "Case #" << caseNumber << ": ";
		string S;
		cin >> S;
		cout << genarateLastWord(S) << endl;
		++caseNumber;
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}