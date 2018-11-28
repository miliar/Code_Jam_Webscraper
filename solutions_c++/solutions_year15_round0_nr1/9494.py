#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_SHY = 1001;

void computeTest (int idTest)
{
	int maxShy;
	scanf("%d", &maxShy);
	int nbShy[MAX_SHY];
	for (int i = 0; i <= maxShy; i++)
	{
		char tmp;
		scanf(" %c", &tmp);
		nbShy[i] = tmp - '0';
	}
		
	int nbCurStandUp = 0;
	int nbFriendNeeded = 0;
	
	for (int i = 0; i <= maxShy; i++)
	{
		if (nbShy[i] == 0)
			continue;
			
		int nbNeeded = max(0, i - nbCurStandUp);
		nbFriendNeeded += nbNeeded;
		nbCurStandUp += nbNeeded + nbShy[i];
	}
	printf("Case #%d: %d\n", idTest+1, nbFriendNeeded);
		
}

int main ()
{
	int nbTest;
	scanf("%d", &nbTest);
	for (int i = 0; i < nbTest; i++)
		computeTest(i);
	
	return 0;
}
