#pragma hdrstop
#pragma argsused

#include <tchar.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include "iostream.h"

unsigned long long gastaResp[10005];

void pre_calcular () {
	for (int i = 2; i <= 10000; i++) {
		gastaResp[i] = i * i - ((i -1) * (i-1));
	}

}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fpIn, *fpOut;
	char cQtd[20];
	int iQtdTotal;

	pre_calcular();

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

	//cout << "Qtd Total: " << iQtdTotal << endl;
    char cSaida[20];

	for (int i=0; i < iQtdTotal; i++) {
		char linha[300];
		char *cpLinha;
		unsigned long long rinicial, ml;
		int raio;
		int cont = 0;

		fgets(linha, 300, fpIn);
		cpLinha = strstr(linha, " ");
		cpLinha++;
		rinicial = strtoull(linha, NULL, 10);
		ml = strtoull(cpLinha, NULL, 10);

		raio = rinicial + 1;

		while (ml >= gastaResp[raio]) {
			ml -= gastaResp[raio];

			raio += 2;
			cont++;
		}
		sprintf(cSaida, "Case #%d: %d\n", i+1, cont);
		fputs(cSaida, fpOut);
	}


	fcloseall();

	system("pause");
}
