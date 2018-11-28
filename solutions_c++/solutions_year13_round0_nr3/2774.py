#pragma hdrstop
#pragma argsused

#include <tchar.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include "iostream.h"
#include <math.h>

bool isPalindrome(__int64 num);
bool isSquare(__int64 num);

int _tmain(int argc, _TCHAR* argv[])
{
	int iQtdTotal;
	char cQtd[20];
	char linha[500];
	char *cpLinha;
	char cSaida[50];
	__int64 num1, num2;
	double iFilho;
	FILE *fpIn, *fpOut;

	fpIn = fopen("sample.in", "r");
	fpOut = fopen("sample.out", "w");

	if (fpIn == NULL)
	{
		std::cout << "Erro ao ler arquivo de entrada!";
		system("pause");
		return 0;
	}
	if (fpOut == NULL)
	{
		cout << "Erro ao ler arquivo de saida!";
 		system("pause");
		return 0;
	}

	fgets(cQtd, 20, fpIn);
	iQtdTotal = strtoul(cQtd, NULL, 10);

	cout << "Qtd Total: " << iQtdTotal << endl;

	//--le caso a caso--//
	for (int i=0; i < iQtdTotal; i++)
	{
		bool bResult;
		double dQuad;
		int cont = 0;

		fgets(linha, 300, fpIn);
		cpLinha = strstr(linha, " ");
		cpLinha++;
		num1 = strtoull(linha, NULL, 10);
		num2 = strtoull(cpLinha, NULL, 10);

		for (__int64 j = num1; j <= num2; j++)
		{
			if (isPalindrome(j))
			{
				if (isSquare(j))
				{
					if(isPalindrome(sqrt((double)j)))
					cont++;
                }
			}
		}

		sprintf(cSaida, "Case #%d: %d\n", i+1, cont);
		fputs(cSaida, fpOut);
    }

	return 0;
}

bool isPalindrome(__int64 num)
{
	__int64 temp = num;
	__int64 inverso = 0;

	while (temp != 0)
	{
		inverso = inverso * 10;
		inverso = inverso + temp%10;
		temp = temp/10;
	}

	if (num == inverso)
	{
		return true;
	}
	else
	{
        return false;
	}
}

bool isSquare(__int64 num)
{
	double dRaiz;

	dRaiz=sqrt((double)num);


	if (dRaiz == (int)dRaiz)
	{
		return true;
	}
	else
	{
        return false;
	}
}