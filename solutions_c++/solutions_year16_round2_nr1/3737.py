
#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <math.h>

int HayNum(char *cadena, int n);

char *Num[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
unsigned char usado[200];


int orden[10] = {0, 2, 4, 6, 5, 8, 9, 3, 7, 1};
unsigned char array1[10];
char salida[21];

int main()
{
	FILE *In, *Out;

	long i, j, k;
	long T;
	char S[200];
	int n;

	int Hay;

	//In = fopen("prueba.in", "r");
	In = fopen("A-small-attempt1.in", "r");
	//In = fopen("A-large.in", "r");

	//Out = fopen("prueba.out", "w");
	Out = fopen("A-small-attempt1.out", "w");
	//Out = fopen("A-large.out", "w");

	fscanf(In, "%ld", &T);
	
	for (i = 0; i < T; i++)
	{
		fscanf(In, "%s", S);
		fprintf(Out, "Case #%d: ", i + 1);

		memset(usado, 0, 200);
		memset(array1, 0, 10);


		for (n = 0; n < 10; n++)
		{
			while (1)
			{
				Hay = HayNum(S, orden[n]);

				if (Hay)
					array1[orden[n]]++;
				else
					break;
			}
		}

		for (j = 0; j < 10; j++)
		{
			for (k = 0; k < array1[j]; k++)
				fprintf(Out, "%d", j);
		}

		fprintf(Out, "\n");

		for (j = 0; S[j]; j++)
		{
			if (!usado[j])
				break;
		}
	}


	fclose(In);
	fclose(Out);

    return 0;
}

int HayNum(char *cadena, int n)
{
	int i, j;
	unsigned char usado1[200];

	memcpy(usado1, usado, 200);

	for (i = 0; Num[n][i]; i++)
	{
		for (j = 0; cadena[j]; j++)
		{
			if (!usado1[j] && cadena[j] == Num[n][i])
			{
				usado1[j] = 1;
				break;
			}
		}
		if (j == strlen(cadena))
			break;
	}

	if (i == strlen(Num[n]))
	{
		for (i = 0; cadena[i]; i++)
			usado[i] |= usado1[i];

		return 1;
	}
	else
		return 0;

}
