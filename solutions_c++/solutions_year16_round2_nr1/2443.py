#include <cstdio>
#include <cstring>
int letter[30] = {0};
int number[15] = {0};


int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("A.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int k = 1; k <= T; k++) {
		int L;
		char s[2005];
		scanf("%d", &L);
		scanf("%s", s);
		memset(letter, 0, sizeof(letter));
		memset(number, 0, sizeof(number));

		for (int i = 0; s[i]; i++)
			letter[s[i] - 64]++;
		number[0] = letter[26];
		number[2] = letter[23];
		number[4] = letter[21];
		number[6] = letter[24];
		number[8] = letter[7];
		number[5] = letter[6] - number[4];
		number[3] = letter[8] - number[8];
		number[7] = letter[22] - number[5];
		number[1] = letter[15] - number[0] - number[2] - number[4];
		number[9] = letter[9] - number[5] - number[6] - number[8];

		printf("Case #%d: ", k);
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < number[i]; j++)
				printf("%d", i);
		}
		printf("\n");
	}

	return 0;
}