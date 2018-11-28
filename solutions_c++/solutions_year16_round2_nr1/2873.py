#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)

#define MAX 2002

FILE *in, *out;
int T;
char S[MAX];
int stringint[26];
int numbercnt[10];

void checknum(char s[30], char a,int number)
{
	int i,j, len;
	len = strlen(s);

	while(stringint[a - 'A']>0)
	{
		for (j = 0; j < len; j++)
		{
			if (stringint[s[j] - 'A'])
			{
				stringint[s[j] - 'A']--;
			}
			else
			{
				for (j = j - 1; j >= 0; j--)
					stringint[s[j] - 'A']++;
				break;
			}
		}
		if (j == len) numbercnt[number]++;
		else break;
	}
	return;
}
void printdigit(){
	for (int i = 0; i < 10; i++)
		if (numbercnt[i])
			for (int j = 0; j < numbercnt[i];j++)
				fprintf(out, "%d", i);

	return;
}
int main()
{

	in = fopen("A-large.in", "r");
	out = fopen("result.txt", "w");

	fscanf(in, "%d", &T);
	for (int a = 1; a <= T; a++){
		int len;
		memset(stringint, 0, sizeof(stringint));
		memset(numbercnt, 0, sizeof(numbercnt));

		fscanf(in,"%s", S);

		len = strlen(S);

		for (int i = 0; i < len; i++) stringint[S[i] - 'A']++;
		
		checknum("ZERO",'Z',0);
		checknum("TWO",'W',2);
		checknum("FOUR", 'U',4);
		checknum("SIX", 'X',6);
		checknum("EIGHT", 'G',8);

		checknum("ONE", 'O',1);
		checknum("THREE", 'T',3);
		checknum("FIVE", 'F',5);
		checknum("SEVEN", 'S',7);

		checknum("NINE", 'N',9);

		fprintf(out, "Case #%d: ", a);
		printdigit();
		fprintf(out, "\n");
	}

	return 0;
}