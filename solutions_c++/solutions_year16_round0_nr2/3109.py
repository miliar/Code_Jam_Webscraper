#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;
/*
int countFlips(string s, int start, int end)
{
	const char* p = s.c_str();
	bool interleaved = false;
	bool allOK = true;

	for (int i = start; i < end; i++)
	{
		if (p[i] == '-')
		{
			allOK = false;
		}
	}

	if (allOK)
	{
		return 0;
	}

	if (interleaved)
	{
		return INT_MAX;
	}

	int minValue = 1;
	for (int i = start; i < end; i++)
	{
		string flippedString = flip(s, start+i, end);
		const char* flipped = flippedString.c_str();
		int newEnd = end - 1;
		do
		{
			if (flipped[newEnd] == '-')
			{
				break;
			}
			newEnd--;
		} while (newEnd >= start);

		minValue = min(minValue, countFlips(flippedString, start, newEnd));
	}

	return minValue;
}
*/
int main() {
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	string s;
	getline(cin, s);

	for (int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";

		getline(cin, s);
		
		char* cstr = const_cast<char*>(s.c_str());
		int counter = 0;

		while (true)
		{
			int numOfCharsToFlip = 0;
			bool flipNeeded = false;
			for (int i = 0; i < s.length()-1; i++)
			{
				numOfCharsToFlip++;

				if (cstr[i] != cstr[i + 1])
				{
					flipNeeded = true;
					counter++;
					break;
				}
			}

			if (!flipNeeded)
			{
				numOfCharsToFlip = 0;
			}

			bool allPositive = true;
			for (int i = 0; i < s.length(); i++)
			{
				if (cstr[i] == '-')
				{
					allPositive = false;
					break;
				}
			}

			if (allPositive)
			{
				break;
			}

			if (numOfCharsToFlip == 0)
			{
				if (!allPositive)
				{
					counter++;
				}

				break;
			}

			// flip
			char* newString = new char[numOfCharsToFlip];			
			for (int i = 0; i < numOfCharsToFlip; i++)
			{
				newString[i] = cstr[numOfCharsToFlip - 1 - i] == '-' ? '+' : '-';
			}

			for (int i = 0; i < numOfCharsToFlip; i++)
			{
				cstr[i] = newString[i];
			}

			delete[] newString;
		}
		

		cout << counter << endl;
	}

	return 0;
}