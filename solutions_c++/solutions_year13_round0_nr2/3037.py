#pragma hdrstop
#pragma argsused

#include <tchar.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include "iostream.h"

int _qtdLinhas, _qtdColunas;

int _tmain(int argc, _TCHAR* argv[])
{
	int iQtdTotal;
	char cTemp[5];	//le a qtd
	char cDim[20];
	char *cpDim, *cpL;
	char l[400][400];	//le as dimensoes
	int lnum[100][100];
	bool lConferidas[100][100];
	char cSaida[20];
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

	fgets(cTemp, 20000, fpIn);
	iQtdTotal = strtoul(cTemp, NULL, 10);

	cout << "Qtd Total: " << iQtdTotal << "\n" << endl;

	//--le caso a caso--//
	for (int i=0; i < iQtdTotal; i++)
	{
		bool bResult = false;
		int maxGrama[100] = {0};
		int qtdGramas = 0;
		bool bRepet;

		//--le as dimensoes (alt e larg) de um determinado caso--//
		fgets(cDim, 20, fpIn);
		cpDim = &cDim[0];
		_qtdLinhas = strtoul(cpDim, NULL, 10);
		cpDim = strstr(cpDim, " ");
		cpDim++;
		_qtdColunas = strtoul(cpDim, NULL, 10);

		//--coleta todo gramado--//
		for (int j=0; j < _qtdLinhas; j++)
		{
			fgets(l[j], 800, fpIn);
			cpL = &l[j][0];
			for (int k=0; cpL!= NULL; k++)
			{
				lnum[j][k] = strtoul(cpL, NULL, 10);
				cpL = strstr(cpL, " ");
				if (cpL == NULL) break;
				cpL++;
			}
		}

		//--pega maior altura do gramado--//
		for (int k=0; k < 100; k++)
		{
			maxGrama[k] = 0;
			for (int linha=0; linha < _qtdLinhas; linha++)
			{
				for (int coluna=0; coluna< _qtdColunas; coluna++)
				{
					if (lnum[linha][coluna] > maxGrama[k])
					{
						bRepet = false;
						for (int procRepet = 0; procRepet <= k; procRepet++)
						{
							if (lnum[linha][coluna] == maxGrama[procRepet]) bRepet = true;
						}
						if (!bRepet)
						{
							maxGrama[k] = lnum[linha][coluna];
							qtdGramas++;
						}
					}
				}
			}
		}

		//--verifica os cortes--//
		//maior tamanho nao precisa ser testado
		bool bResp = true;
		for (int linha=0; linha < _qtdLinhas; linha++)
		{
			for (int coluna=0; coluna< _qtdColunas; coluna++)
			{
				lConferidas[linha][coluna] = false;
			}
		}
		for (int g=0; g < qtdGramas; g++)
		{
			//varre toda o gramado em busca da grama da vez, se encontrado
			//verifica se nao existe maior ou na linha ou na coluna
			for (int linha=0; linha < _qtdLinhas; linha++)
			{
				for (int coluna=0; coluna< _qtdColunas; coluna++)
				{
					if (lnum[linha][coluna] == maxGrama[g])
					{
						bool bResp1 = true;
						bool bResp2 = true;
						lConferidas[linha][coluna] = true;
						//linhas
						for (int lin=0; lin < _qtdLinhas; lin++) {
							if (lnum[lin][coluna] > maxGrama[g])/* &&
								lConferidas[lin][coluna] == false)*/
							{
								bResp1 = false;
							}
						}
						//colunas
						for (int col=0; col < _qtdColunas; col++) {
							if (lnum[linha][col] > maxGrama[g])/* &&
								lConferidas[linha][col] == false)*/
							{
								bResp2 = false;
							}
						}
						if (!bResp1 && !bResp2) {
							bResp = false;
						}
					}
				}
			}
		}
		//ok
		if (bResp) {
			sprintf(cSaida, "Case #%d: YES\n", i+1);
		}
		else
		{
			sprintf(cSaida, "Case #%d: NO\n", i+1);
		}
		fputs(cSaida, fpOut);
	}

	fcloseall();
	return 0;
}

