#include <cstdio>

using namespace std;

int main()
{
	int nbTests;
	scanf("%d", &nbTests);
	for(int iTest = 1; iTest <= nbTests; ++iTest)
	{
		int timMax;
		int nbDeb = 0;
		int extra = 0;
		scanf("%d ", &timMax);
		for(int iTim = 0; iTim <= timMax; ++iTim)
		{
			char nbPer;
			scanf("%c", &nbPer);
			while(nbPer != '0' && nbDeb < iTim)
			{
				++nbDeb;
				++extra;	
			}
			nbDeb += nbPer - '0';
		}
		printf("Case #%d: %d\n", iTest, extra);
	}
	return 0;
}
