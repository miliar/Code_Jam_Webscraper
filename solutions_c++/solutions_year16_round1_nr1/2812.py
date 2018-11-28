#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

using namespace std;

int main()
{
	long long T;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		int i;
		string S, lastWord;
		
		cin >> S;
		lastWord = S[0];

		for (i = 1; i < S.length(); i++)
		{
			if (S[i] >= lastWord[0])
				lastWord = S[i] + lastWord;
			else
				lastWord = lastWord + S[i];
		}

		cout << "Case #" << t << ": " << lastWord << endl;
	}

	return 0;
}

#endif