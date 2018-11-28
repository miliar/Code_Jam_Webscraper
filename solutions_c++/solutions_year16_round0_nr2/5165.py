#include <iostream>
#include <vector>
#include <string>

using namespace std;
#pragma warning(disable:4996)

typedef unsigned int uint;

uint getTheFlipCount(const string& S)
{
	uint flipCount = 0;
	bool plusFound = false;
	for (auto it = begin(S); it != end(S);)
	{
		if (*it == '+')
		{
			plusFound = true;
			++it;
		}
		else
		{
			while ((it != end(S)) && *it == '-')
			{
				++it;
			}
			if (plusFound)
				flipCount += 2;
			else
				flipCount += 1;

			plusFound = true;
		}
	}
	return flipCount;
}

int main()
{
	freopen("C:\\Users\\Dilum\\Desktop\\SingaJob\\GoogleCodeJam_2016\\Debug\\input.in", "r", stdin);
	freopen("C:\\Users\\Dilum\\Desktop\\SingaJob\\GoogleCodeJam_2016\\Debug\\output.txt", "w", stdout);

	uint testCases;
	cin >> testCases;
	uint caseNumber = 1;

	vector<bool> panckakeStack;
	while (caseNumber <= testCases)
	{
		panckakeStack.clear();

		string S;
		cin >> S;
		uint plusCount = 0;
		uint strLength = S.length();
		for (unsigned i = 0; i < strLength; ++i)
		{
			if (S[i] == '+')
				++plusCount;
		}

		if (plusCount == strLength)
		{
			cout << "Case #" << caseNumber << ": " << 0 << endl;
			++caseNumber; 
			continue;
		}

		if (plusCount == 0)
		{
			cout << "Case #" << caseNumber << ": " << 1 << endl;
			++caseNumber;
			continue;
		}
		
		uint flipCountWithoutReverse = 0;
		flipCountWithoutReverse = getTheFlipCount(S);

		uint flipCountWithReverse = 0;
		if (plusCount < (strLength - plusCount))
		{
			string newString;
			newString.resize(strLength, '+');
			for (uint i = 0; i < strLength; ++i)
			{
				if (S[i] == '+')
				{
					newString[strLength - i - 1] = '-';
				}
			}
			S = newString;
			++flipCountWithReverse;
		}
		flipCountWithReverse += getTheFlipCount(S);
		
		uint flipCount = (flipCountWithoutReverse < flipCountWithReverse) ? flipCountWithoutReverse: flipCountWithReverse;
		cout << "Case #" << caseNumber << ": " << flipCount << endl;
		++caseNumber;
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}