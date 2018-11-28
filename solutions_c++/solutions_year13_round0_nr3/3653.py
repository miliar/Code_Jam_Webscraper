#include <cstdio>
#include<algorithm>
#include <cmath>

using namespace std;

FILE *fout;
FILE *fin;

int curPal[100 + 3];
int nbPals = 0;
unsigned long long bInf, bSup;

bool estPal(unsigned long long curP)
{
	int pal[100 + 1] = {0};
	unsigned long long puissDeDix = 10;
	int curD = 0;
	while(curP / (puissDeDix / 10) > 0)
	{
		pal[curD] = (curP % puissDeDix) * 10 / puissDeDix;
		curP -= (curP % puissDeDix);
		puissDeDix *= 10;
		curD++;
	}
	//fprintf(fout, "curD : %d\n", curD);
	/*for(int curC = 0; curC < curD; curC++)
		fprintf(fout, "%d ", pal[curC]);*/
	for(int curC = 0; curC < curD; curC++)
		if(pal[curC] != pal[curD - curC - 1])
			return 0;
	return 1;
}

void testPal(int nbCTot)
{
	/*fprintf(fout, "curPal : \n");
	for(int curC = 0; curC < nbCTot; curC++)
		fprintf(fout, "%d", curPal[curC]);*/
	unsigned long long valPal = 0;
	unsigned long long puissDix = 1;
	for(int curC = 0; curC < nbCTot; curC++)
	{
		valPal += (curPal[curC] * puissDix);
		puissDix *= 10;
	}
	if(valPal < bInf || valPal > bSup)
	{
		//fprintf(fout, "dehors\n");
		return;
	}
	unsigned long long valRac = sqrt(double(valPal));
	if(valRac * valRac != valPal)
	{
		//fprintf(fout, "pas carre parfait\n");
		return;
	}
	int test = estPal(valRac);
	nbPals += test;
	//fprintf(fout, "teste : %d\n", test);

}

void generePal(int nbCTot, int nbCM)
{
	if(nbCM == nbCTot / 2)
	{
		if(nbCTot % 2 == 0)
		{
			testPal(nbCTot);
			return;
		}
		else
		{
			for(int curC = 0; curC < 10; curC++)
			{
				curPal[nbCTot / 2] = curC;
				testPal(nbCTot);
			}
			return;
		}
	}
	for(int curC = 0; curC < 10; curC++)
	{
		curPal[nbCM] = curC;
		curPal[nbCTot - nbCM - 1] = curC;
		generePal(nbCTot, nbCM + 1);
	}
}

void trouveSol(int curT)
{
	nbPals = 0;
	fscanf(fin, "%llu%llu", &bInf, &bSup);
	unsigned long long curDix = 1;
	int nbCMin = -1;
	int nbCMax = -1;
	for(int curD = 0; curD <= 100; curD++)
	{
		if(bInf / curDix == 0 && nbCMin == -1)
			nbCMin = curD;
		if(bSup / curDix == 0)
		{
			nbCMax = curD;
			break;
		}
		curDix *= 10;
	}
	//fprintf(fout, "\n\nnbCMin : %d et nbCMax : %d\n\n", nbCMin, nbCMax);
	for(int curNbC = nbCMin; curNbC <= nbCMax; curNbC++)
		generePal(curNbC, 0);
	fprintf(fout, "Case #%d: %d\n", curT, nbPals);
}

int main()
{
	fin = fopen ("C-Small.in", "r");
	fout = fopen ("C-Small.out", "w");

	int nbTests;
	fscanf(fin, "%d", &nbTests);
	for(int curT = 1; curT <= nbTests; curT++)
	{
		trouveSol(curT);
	}
	//estPal(676);
    return 0;
}
