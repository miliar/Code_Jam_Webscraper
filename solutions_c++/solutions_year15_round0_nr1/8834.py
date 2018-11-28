#include<iostream>
#include<cstdio>

using namespace std;

int main(void)
{
	int T, i, j, k, l, m, Smax, noPpl, pplStanding, frnds;
	char c;
	freopen("aBig.in", "r", stdin);
	freopen("aBig.out", "w", stdout);
	scanf("%d", &T);
	for(i=0; i<T; i++)
	{
		pplStanding=0, frnds=0;
		scanf("%d", &Smax);
		for(j=0; j<=Smax; j++)
		{
			do{
				scanf("%c", &c);
			}while(c-'0'==-16);
			noPpl = c - '0';
			//scanf("%d", &noPpl);
			if(noPpl>0)
			{
				if(pplStanding<j)
				{
					frnds = frnds + (j-pplStanding);
					pplStanding = pplStanding + (j-pplStanding);
				}
				pplStanding = pplStanding + noPpl;	
			}
		}
		printf("Case #%d: %d\n", i+1, frnds);
	}
	return 0;
}
