#define _CRT_SECURE_NO_WARNINGS

#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

typedef unsigned long long ull_t;

int main(int argc, char* argv[])
{
	freopen("in.txt", "rb", stdin);
	freopen("out.txt", "wb", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);

		const int MAX_L = 2000;
		char s[MAX_L + 1];
		scanf ("%s", s);

		int counts['Z' + 1];
		int digits_counts[10];
		memset(counts, 0, sizeof(counts));
		memset(digits_counts, 0, sizeof(digits_counts));

		for (int i = 0; s[i] != '\0'; i++)
		{
			counts[s[i]]++;
		}

		struct
		{
			int digit;
			char letter;
			const char *digit_name;
		} decoder_descr[10] = 
			{
				{ 0, 'Z', "ZERO" },
				{ 2, 'W', "TWO" },
				{ 4, 'U', "FOUR" },
				{ 6, 'X', "SIX" },
				{ 8, 'G', "EIGHT" },
				{ 7, 'S', "SEVEN" },
				{ 5, 'V', "FIVE" },
				{ 3, 'T', "THREE" },
				{ 9, 'I', "NINE" },
				{ 1, 'O', "ONE" },
			};

		for (int i = 0; i < 10; i++)
		{
			int cnt = counts[decoder_descr[i].letter];
			digits_counts[decoder_descr[i].digit] += cnt;

			const char *name = decoder_descr[i].digit_name;
			for (int j = 0; name[j] != '\0'; j++)
			{
				counts[name[j]] -= cnt;
			}
		}

		for (int i = 0; i < 10; i++)
		{
			for (int j = 0; j < digits_counts[i]; j++)
			{
				printf("%d", i);
			}
		}

		printf("\n");
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
