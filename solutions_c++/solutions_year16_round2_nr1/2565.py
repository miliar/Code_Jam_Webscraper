#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;

int main() {
	FILE *fin = freopen("A-large1.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	string s;
	getline(cin, s);

	for (int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";

		getline(cin, s);		
		
		char* cstr = const_cast<char*>(s.c_str());
		int digits[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

		for (int i = 0; i < s.length(); i++)
		{
			if (cstr[i] == 'Z')
			{
				digits[0]++;
				continue;
			}
			if (cstr[i] == 'W')
			{
				digits[2]++;
				continue;
			}
			if (cstr[i] == 'X')
			{
				digits[6]++;
				continue;
			}
			if (cstr[i] == 'U')
			{
				digits[4]++;
				continue;
			}
			if (cstr[i] == 'G')
			{
				digits[8]++;
				continue;
			}
		}

		int numOfFours = digits[4];
		int numOfEights = digits[8];

		for (int i = 0; i < s.length(); i++)
		{
			if (cstr[i] == 'F')
			{
				if (numOfFours > 0)
				{
					numOfFours--;
				}
				else
				{
					digits[5]++;
				}
			}

			if (cstr[i] == 'H')
			{
				if (numOfEights > 0)
				{
					numOfEights--;
				}
				else
				{
					digits[3]++;
				}
			}
		}

		int numOfFives = digits[5];

		for (int i = 0; i < s.length(); i++)
		{
			if (cstr[i] == 'V')
			{
				if (numOfFives > 0)
				{
					numOfFives--;
				}
				else
				{
					digits[7]++;
				}
			}
		}

		numOfFives = digits[5];
		numOfEights = digits[8];
		int numOfSix = digits[6];
		int numOfZeros = digits[0];
		int numOfTwos = digits[2];
		numOfFours = digits[4];

		for (int i = 0; i < s.length(); i++)
		{
			if (cstr[i] == 'I')
			{
				if (numOfFives > 0)
				{
					numOfFives--;
				}
				else if (numOfSix > 0)
				{
					numOfSix--;
				}
				else if (numOfEights> 0)
				{
					numOfEights--;
				}
				else
				{
					digits[9]++;
				}
			}

			if (cstr[i] == 'O')
			{
				if (numOfZeros > 0)
				{
					numOfZeros--;
				}
				else if (numOfTwos > 0)
				{
					numOfTwos--;
				}
				else if (numOfFours> 0)
				{
					numOfFours--;
				}
				else
				{
					digits[1]++;
				}
			}
		}

		for (int i = 0; i < 10; i++)
		{
			for (int j = 0; j < digits[i]; j++)
			{
				cout << i;
			}
		}

		cout << endl;
	}

	return 0;
}