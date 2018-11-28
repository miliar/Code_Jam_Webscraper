#include <algorithm>
#include <cmath>
#include <cstdio>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

const int oo = 1000*1000*1000;
const int MAX_CUBES = 1000;

int nbCubes, nbTests;
double cubesNaomi[MAX_CUBES];
double cubesKen[MAX_CUBES];
int iNaomi, debKen, finKen;

void computeAnswer()
{
	for(int iTest = 0; iTest < nbTests; ++iTest)
	{
		scanf("%d", &nbCubes);
		for(int iCube = 0; iCube < nbCubes; ++iCube)
			scanf("%lf", &cubesNaomi[iCube]);
		for(int iCube = 0; iCube < nbCubes; ++iCube)
			scanf("%lf", &cubesKen[iCube]);
		sort(cubesNaomi, cubesNaomi+nbCubes);
		sort(cubesKen, cubesKen+nbCubes);
		/*for(int iCube = 0; iCube < nbCubes; ++iCube)
			printf("%lf ", cubesNaomi[iCube]);
		printf("\n");
		for(int iCube = 0; iCube < nbCubes; ++iCube)
			printf("%lf ", cubesKen[iCube]);
		printf("\n");*/
		iNaomi = 0; debKen = 0; finKen = nbCubes-1;
		int total = 0;
		while(iNaomi < nbCubes && finKen >= debKen)
		{
			if(cubesNaomi[iNaomi] < cubesKen[debKen])
			{
				++iNaomi; --finKen;
			}
			else
			{
				++total;
				++iNaomi; ++debKen;
			}
		}
		printf("Case #%d: %d ", iTest+1, total);
		total = 0;
		debKen = 0; finKen = nbCubes-1;
		for(int iCube = nbCubes-1; iCube >= 0; --iCube)
		{
			if(cubesNaomi[iCube] > cubesKen[finKen])
			{
				++total;
				++debKen;
			}
			else
				--finKen;
		}
		printf("%d\n", total);
	}
}

void readInput()
{
	//*
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	//*/
	scanf("%d", &nbTests);
}

int main()
{
	readInput();
	computeAnswer();
	return 0;
}
