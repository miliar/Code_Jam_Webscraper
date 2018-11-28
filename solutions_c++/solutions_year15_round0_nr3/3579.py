#include<stdio.h>
#include <math.h>
#include <stdlib.h>

char quarternions(char a, char b, int *sign);

int main()
{
	FILE* inputFile;
	FILE* outputFile;
	int T = 0;
	int L = 0, X = 0;
	char *ret;
	char y[10] = "YES";
	char n[10] = "NO";
	char input[10001];
	long long i,j,k;
	int Sign = 1;
	int *sign = &Sign;
	char temp;
	int getI=0, getJ=0;
	fopen_s(&inputFile, "C-small-attempt4.in", "rt");
	fopen_s(&outputFile, "C-small-attempt4.txt", "wt");

	if (inputFile == NULL)
	{
		printf_s("error");
	}
	else
	{
		fscanf_s(inputFile, "%d", &T);

		printf("%d\n", T);
	}


	for (i = 0; i < T; i++)
	{
		fscanf_s(inputFile, "%d ", &L);
		fscanf_s(inputFile, "%d ", &X);
		fscanf_s(inputFile, "%s", input,sizeof(input));
		//printf("input : %s\n", input);

		temp = '1';
		Sign = 1;
		getI = 0;
		getJ = 0;

		for (k = 0; k < X; k++)
		{
			for (j = 0; j < L; j++)
			{
				temp = quarternions(temp, input[j], sign);
				//printf("%c", temp);
				if (temp == 'i' && getI == 0)
				{
					temp = '1';
					getI = 1;
				}
				if (temp == 'j' && getI == 1 && getJ == 0)
				{
					temp = '1';
					getJ = 1;
				}
			}
		}
		//printf("\n");

		if (getJ == 1 && temp == 'k' && Sign == 1)
		{
			ret = y;
		}
		else
		{
			ret = n;
		}

		printf_s("Case #%lld: %s\n", i + 1, ret);
		fprintf_s(outputFile, "Case #%lld: %s\n", i + 1, ret);
	}

	fclose(inputFile);
	fclose(outputFile);

//	scanf_s("%d", &i);

	return 0;
}

char quarternions(char a, char b, int *sign)
{
	if (a == '1' && b == 'i')
	{
		return 'i';
	}
	if (a == '1' && b == 'j')
	{
		return 'j';
	}
	if (a == '1' && b == 'k')
	{
		return 'k';
	}
	if (a == 'i' && b == 'i')
	{
		*sign *= -1;
		return '1';
	}
	if (a == 'i' && b == 'j')
	{
		return 'k';
	}
	if (a == 'i' && b == 'k')
	{
		*sign *= -1;
		return 'j';
	}
	if (a == 'j' && b == 'i')
	{
		*sign *= -1;
		return 'k';
	}
	if (a == 'j' && b == 'j')
	{
		*sign *= -1;
		return '1';
	}
	if (a == 'j' && b == 'k')
	{
		return 'i';
	}
	if (a == 'k' && b == 'i')
	{
		return 'j';
	}
	if (a == 'k' && b == 'j')
	{
		*sign *= -1;
		return 'i';
	}
	if (a == 'k' && b == 'k')
	{
		*sign *= -1;
		return '1';
	}

}

