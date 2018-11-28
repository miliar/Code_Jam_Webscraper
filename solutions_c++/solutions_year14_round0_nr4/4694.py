#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_BLOCS = 1000;

void game (int curGame)
{
	int nbBlocs;
	scanf("%d", &nbBlocs);

	double blocsNaomi[MAX_BLOCS], blocsKen[MAX_BLOCS];

	for (int iBloc = 0; iBloc < nbBlocs; iBloc++)
	{
		scanf("%lf", &blocsNaomi[iBloc]);
	}
	for (int iBloc = 0; iBloc < nbBlocs; iBloc++)
	{
		scanf("%lf", &blocsKen[iBloc]);
	}

	sort(blocsNaomi, blocsNaomi+nbBlocs);
	sort(blocsKen, blocsKen + nbBlocs);

	int nbPointsKenWar = 0;
	int posKen = 0;
	for (int iBloc = 0; iBloc < nbBlocs; iBloc++)
	{
		int ok = 1;
		while (1)
		{
			if (posKen >= nbBlocs)
			{
				ok = 0;
				break;
			}
			if (blocsKen[posKen] > blocsNaomi[iBloc])
				break;
			posKen++;
		}
		if (ok)
			nbPointsKenWar++;
		posKen++;
	}

	int nbPointsNaomiWar2 = 0;
	posKen = 0;
	for (int iBloc = 0; iBloc < nbBlocs; iBloc++)
		if (blocsNaomi[iBloc] > blocsKen[posKen])
		{
			posKen++;
			nbPointsNaomiWar2++;
		}

	printf("Case #%d: %d %d\n", curGame, nbPointsNaomiWar2, nbBlocs - nbPointsKenWar);
			
	return;
}

int main ()
{
	int nbGame;
	scanf("%d", &nbGame);

	for (int iGame = 0; iGame < nbGame; iGame++)
		game(iGame+1);



	return 0;
}
