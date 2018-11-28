#pragma hdrstop
#pragma argsused

#include <tchar.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include "iostream.h"

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fpIn, *fpOut;
	char cQtd[20];
	int iQtdTotal;

	//pre_calcular();

	fpIn = fopen("A-small-attempt6.in", "r");
	fpOut = fopen("Aaaa.out", "w");

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

	for (int aaa=0; aaa < iQtdTotal; aaa++) {
		char linha[300];
		char *cpLinha;
		int am;
		int oq;         //others qtd
		int om[110];
		int cp = 0;		//cont(qtd) percorridos
		int co = 0;		//cont(qtd) operacoes
		int maxo;		//max others
		int contretiratodos;
		bool addum;
		int oqorig;

		fgets(linha, 300, fpIn);
		cpLinha = strstr(linha, " ");
		cpLinha++;
		am = strtoul(linha, NULL, 10);		//armin_mote
		oq = strtoul(cpLinha, NULL, 10);	//others_qtd
		oqorig = oq;

		fgets(linha, 300, fpIn);
		om[0] = strtoul(linha, NULL, 10);
		cpLinha = strstr(linha, " ");
		cpLinha++;
		//armazena outro motes na variavel
		for (int i=1; i < oq; i++) {
			om[i] = strtoul(cpLinha, NULL, 10);//others_mote
			cpLinha++;
			cpLinha = strstr(cpLinha, " ");
		}
		while (cp < oqorig) {
			if (am == 1) {
				sprintf(cSaida, "Case #%d: %d\n", aaa+1, oq);
				fputs(cSaida, fpOut);
				break;
			}
			//come os outros motes
			int i;
			for (i=0; i < oq; i++) {
				if (am > om[i] && om[i] > 0) {
					am += om[i];
					om[i] = 0;
					i=-1;
					cp++;
				}
			}
			//verifica o q sobrou
			if (cp == oq) {
				//saida
				int resp;
				if (contretiratodos > 0 && contretiratodos<co) resp = contretiratodos;
				else resp = co;
				sprintf(cSaida, "Case #%d: %d\n", aaa+1, resp);
				fputs(cSaida, fpOut);
			}
			else if (cp == oq -1){
				int resp;
				if (contretiratodos > 0 && contretiratodos<co+1) resp = contretiratodos;
				else resp = co+1;
				sprintf(cSaida, "Case #%d: %d\n", aaa+1, resp);
				fputs(cSaida, fpOut);
				cp= oq;
			}
			else{
				int min = 100;

				for (int i=0; i < oq; i++) {
					if (om[i] > 0 && min>om[i]) min = om[i];
				}
				//aqui temos o menor de todos
				if (min >= am * 2 - 1) {  //se tem que retirar todos
					contretiratodos = oq-cp;
					//cp = oq;
				}
				//coloca um mote no adversario
				addum = false;
				for (i=0; i < oq; i++) {
					if (om[i] == 0) {
						om[i] = am-1;
						cp--;
						addum = true;
						break;
					}
				}
				if (addum == false){
					om[oq] = am-1;
					oq++;
				}
				co++;
			}
		}
	}


	fcloseall();

	system("pause");
}
