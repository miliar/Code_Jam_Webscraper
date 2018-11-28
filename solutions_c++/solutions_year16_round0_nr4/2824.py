#include <iostream>
#include <cmath>
using namespace std;
typedef unsigned long long ull;

int main() 
{
	int numTestCases;
	scanf("%d", &numTestCases);
	for (int t = 0; t < numTestCases; t++) 
	{
		int artSize, complexity, maxTries;
		scanf("%d %d %d", &artSize, &complexity, &maxTries);

		printf("Case #%d:", t+1);
		if (artSize > complexity * maxTries)
		{
			printf(" IMPOSSIBLE\n");
			continue;
		}
		int numTries = ceil(1.0*artSize / complexity);
		int numCheckedTiles = 0;
		for (int i = 0; i < numTries; i++)
		{
			ull pos = 0;
			ull blockSize = pow(artSize, complexity - 1);
			for (int j = 0; j < complexity; j++)
			{
				if (numCheckedTiles < artSize)
				{
					pos += blockSize * numCheckedTiles;
					numCheckedTiles++;
				}
				blockSize /= artSize;
			}
			printf(" %llu", pos+1);
		}			
		printf("\n");
	}
	return 0;
}