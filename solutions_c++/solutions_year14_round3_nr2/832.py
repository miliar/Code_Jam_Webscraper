#include <cstdio>
#include <algorithm>
#include <set>
#include <cmath>
#include <iostream>
#include <string>

using namespace std;

int permut(string prefix, string *moreStrings, unsigned int *stringsUsed, unsigned int stringCount, unsigned int doneYet)
{
	if (doneYet == 0)
	{
		int char_flags[26] = {0};
		char current_char = prefix[0];
		for (unsigned int letter = 1; letter < prefix.size(); ++letter)
		{
			if (prefix[letter] != current_char)
			{
				if (char_flags[prefix[letter] - 'a'] == 1)
				{
					return 0;
				}

				char_flags[current_char - 'a'] = 1;
				current_char = prefix[letter];
			}
		}

		return 1;
	}
	else
	{
		unsigned long permutations = 0;
		for (unsigned int i = 0; i < stringCount; ++i)
		{
			if (stringsUsed[i] == 0)
			{
				stringsUsed[i] = 1;
				permutations += permut(prefix + moreStrings[i], moreStrings, stringsUsed, stringCount, doneYet - 1);
				stringsUsed[i] = 0;
			}
		}
		return  permutations;
	}
}

int main(void)
{
	unsigned int test_count;
	scanf("%u\n", &test_count);

	for (unsigned int test = 0; test < test_count; ++test)
	{
		printf("Case #%u: ", test + 1);

		unsigned int carSetCount;;
		scanf("%u\n", &carSetCount);

		string carSets[100];
		for (unsigned int i = 0; i < carSetCount; ++i)
		{
			cin >> carSets[i];
		}

		//gen pernutations
		unsigned int stringsUsed[100] = {0};
		unsigned long permutations = permut(string(), carSets, stringsUsed, carSetCount, carSetCount);

		cout << permutations << endl;
	}
}
