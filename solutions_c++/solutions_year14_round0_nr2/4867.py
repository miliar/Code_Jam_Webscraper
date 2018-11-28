#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

void cookie (int curTry)
{
	double objectif, coutFerme, bonusFerme;
	scanf("%lf%lf%lf", &coutFerme, &bonusFerme, &objectif);

	double curTemps = 0, curCookie = 0, curBonus = 2;
	while (curCookie < objectif)
	{
		double nbCookieAObtenir = objectif - curCookie;
		double tempsSansFerme = nbCookieAObtenir/curBonus;
		double tempsAvecFerme = (max(coutFerme-curCookie,(double)0)/curBonus) + (objectif - max(curCookie-coutFerme,(double)0)) / (curBonus + bonusFerme);

		if (tempsSansFerme < tempsAvecFerme) // Inutile d'acheter une ferme
		{
			curCookie = objectif;
			curTemps += tempsSansFerme;
		}
		else
		{
			curTemps += (max(coutFerme-curCookie,(double)0)/curBonus);
			//Puis on achète la ferme
			curCookie += (max(coutFerme-curCookie,(double)0)/curBonus) * curBonus;
			curCookie -= coutFerme;
			curBonus += bonusFerme;
		}
	}

	printf("Case #%d: %.7f\n", curTry, curTemps);
}	

int main ()
{
	int nbTentatives;
	scanf("%d", &nbTentatives);

	for (int iTry = 0; iTry < nbTentatives; iTry++)
		cookie(iTry+1);


	return 0;
}
