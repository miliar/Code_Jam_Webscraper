#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

#define MAXP 1002

int cas,T;
int N,P[MAXP],total,maxP,most;

int main()
{
	freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);

	scanf("%d", &T);
	for (cas = 1; cas <= T; ++cas)
	{
		scanf("%d", &N);
		total = 0;
		for (int i = 0; i < N; ++i)
		{
			scanf("%d", &P[i]);
			total += P[i];
		}
		printf("Case #%d:", cas);
		while(total > 0)
		{
			maxP = 0;
			most = 0;
			for (int i = 0; i < N; ++i)
			{
				if (P[i] > maxP)
				{
					maxP = P[i];
					most = 1;
				}
				else if (P[i] == maxP)
				{
					++most;
				}
			}
			if (most != 2)
			{
				for (int i = 0; i < N; ++i)
				{
					if (P[i] == maxP)
					{
						printf(" %c", 'A'+i);
						--P[i];
						break;
					}
				}
				--total;
			}
			else
			{
				printf(" ");
				for (int i = 0; i < N; ++i)
				{
					if (P[i] == maxP)
					{
						printf("%c", 'A'+i);
						--P[i];
					}
				}
				total -= 2;
			}
		}

		printf("\n");
	}
	
	return 0;
}