
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>

#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

#define IN_FILE_NAME "A-large.in"
#define OUT_FILE_NAME "A-large.out"

static const int MAXS = 2005;

int letters[27];

typedef struct _ID{
	char id;
	char letters[10];
	int nr;
}ID;

int main()
{
	freopen(IN_FILE_NAME, "r", stdin);
	freopen(OUT_FILE_NAME, "w", stdout);

	int t, tests;
	scanf("%d", &tests);

	ID ids[10] = {
		{'Z', "ZERO", 0},
		{'X', "SIX", 6},
		{'S', "SEVEN", 7},
		{'V', "FIVE", 5},
		{'F', "FOUR", 4},
		{'G', "EIGHT", 8},
		{'H', "THREE", 3},
		{'T', "TWO", 2},
		{'O', "ONE", 1},
		{'N', "NINE", 9}
	};

	for(t=0; t<tests; t++)
	{
		char s[MAXS];
		int len;
		int digits[2000];
		int digitIdx = 0;

		memset(letters, 0, sizeof(letters));

		scanf("%s", s);
		len = strlen(s);

		for(int i=0; i<len; i++)
		{
			letters[s[i]-'A']++;
		}
		
		for(int i=0; i<10; i++)
		{
			ID id = ids[i];
			while(letters[id.id - 'A'] > 0)
			{
				for(int k=0; id.letters[k] != 0; k++)
				{
					letters[id.letters[k] - 'A']--;
				}
				digits[digitIdx++] = id.nr;
			}
		}

		sort(digits, digits+digitIdx);

		printf("Case #%d: ", t+1);
		for(int i=0; i<digitIdx; i++)
		{
			printf("%d", digits[i]);
		}
		printf("\n");
	}
}