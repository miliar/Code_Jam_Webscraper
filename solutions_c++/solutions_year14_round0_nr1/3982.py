#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#define REP(I,N) for(int I = 0; I < N; ++I)
#define REPN(I,N) for(int I = 1; I <= N; ++I)
using namespace std;
typedef vector<int> VI;

int main()
{
	int ileTestow, guess, tmp, znalezione = -1;
	VI wektor;
	bool wolontariuszKlamie = false;
	
	scanf("%d", &ileTestow);
	REPN(i, ileTestow)
	{
		scanf("%d", &guess);
		REPN(j, 4)
		{
			if(j == guess)
			{
				REP(k, 4)
				{
					scanf("%d", &tmp);
					wektor.push_back(tmp);
				}
			}
			
			else scanf("%d %d %d %d", &tmp, &tmp, &tmp, &tmp);
		}
		
		scanf("%d", &guess);
		REPN(j, 4)
		{
			if(j == guess)
			{
				REP(k, 4)
				{
					scanf("%d", &tmp);
					if((find(wektor.begin(), wektor.end(), tmp)) != wektor.end())
					{
						if(znalezione == -1) znalezione = tmp;
						else wolontariuszKlamie = true;
					}
				}
			}
			
			else scanf("%d %d %d %d", &tmp, &tmp, &tmp, &tmp);
		}
		
		printf("Case #%d: ", i);
		if(znalezione == -1) printf("Volunteer cheated!\n");
		else if(wolontariuszKlamie) printf("Bad magician!\n");
		else printf("%d\n", znalezione);
		
		wolontariuszKlamie = false;
		znalezione = -1;
		wektor.clear();
	}
}
