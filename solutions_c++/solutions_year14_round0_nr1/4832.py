#include <cstdlib>
#include <cstdio>

using namespace std;

int nbInput;

const int NB_CARD = 16;

void repondreQuestion (int curTest)
{
	int ligne1, ligne2, nbOk[NB_CARD];

	scanf("%d", &ligne1);

	for (int iCard = 0; iCard < NB_CARD; iCard++)
	{
		int val;
		scanf("%d", &val);
		--val;
		nbOk[val] = 0;
		if (iCard >= 4*(ligne1-1) && iCard < 4*ligne1)
			nbOk[val]++;
	}

	scanf("%d", &ligne2);

	for (int iCard = 0; iCard < NB_CARD; iCard++)
	{
		int val;
		scanf("%d", &val);
		--val;

		if (iCard >= 4*(ligne2-1) && iCard < 4*ligne2)
			nbOk[val]++;
	}

	int nbCartesValides = 0;

	for (int iCard = 0; iCard < NB_CARD; iCard++)
		if (nbOk[iCard] == 2)
			nbCartesValides++;

	if (nbCartesValides == 0)
		printf("Case #%d: Volunteer cheated!\n", curTest);
	else if (nbCartesValides >= 2)
		printf("Case #%d: Bad magician!\n", curTest);
	else
	{
		int idCarteOk;
		for (int iCard = 0; iCard < NB_CARD; iCard++)
			if (nbOk[iCard] == 2)
				idCarteOk = iCard+1;

		printf("Case #%d: %d\n", curTest, idCarteOk);
	}

	return;
}

int main ()
{
	scanf("%d", &nbInput);

	for (int input = 0; input < nbInput; input++)
	{
		repondreQuestion(input+1);
	}


	return 0;
}
