
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <tuple>

using namespace std;


#define ASSERT(X) {if (!(X)) {printf("\n assertion failed at line %d\n",__LINE__);exit(0);}}

float naomi[1001];
float ken[1001];

float naomi_cheat[1001];
float ken_cheat[1001];

int compare(const void* a, const void* b)
{
	float int_a = *((float*)a);
	float int_b = *((float*)b);

	if (int_a == int_b) return 0;
	else if (int_a < int_b) return -1;
	else return 1;
}


int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);

	int testcase;
	scanf("%d", &testcase);
	for (int case_id = 1; case_id <= testcase; case_id++)
	{
		int n = 0;
		int y = 0;
		int z = 0;

		for (int i = 0; i < 1001; i++)
		{
			naomi[i] = 0;
			naomi_cheat[i] = 0;
			ken[i] = 0;
			ken_cheat[i] = 0;
		}

		printf("Case #%d: ", case_id);
		scanf("%d", &n);

		for (int i = 0; i < n; i++)
		{
			scanf("%f", &naomi[i]);
		}

		for (int i = 0; i < n; i++)
		{
			scanf("%f", &ken[i]);
		}

		//Trier
		qsort(naomi, n, sizeof(float), compare);
		qsort(ken, n, sizeof(float), compare);

		for (int i = 0; i < n; i++)
		{
			naomi_cheat[i] = naomi[i];
			ken_cheat[i] = ken[i];
		}

		while (n > 0)
		{
			//Version correct

			//Naomi prend tjs le plus lourd
			float naomi_block = naomi[n-1];

			float ken_block = 0;

			for (int i = 0; i < n; i++)
			{
				if (ken[i] > naomi_block)
				{
					ken_block = ken[i];
					for (int j = i; j < (n - 1); j++)
					{
						ken[j] = ken[j + 1];
					}
					break;
				}
			}

			if (ken_block == 0)
			{
				ken_block = ken[0];
				z++;

				for (int j = 0; j < (n - 1); j++)
				{
					ken[j] = ken[j + 1];
				}
			}



			//Version triche



			//Si elle a le plus petit elle joue sans tricher
			//if ()
			//{
			

			
			//printf("\nNaomi: %f", naomi_cheat[0]);
				

			if (naomi_cheat[0] > ken_cheat[0])
			{
				//printf(" Ken: %f", ken_cheat[0]);
				y++;

				for (int j = 0; j < (n - 1); j++)
				{
					naomi_cheat[j] = naomi_cheat[j + 1];
					ken_cheat[j] = ken_cheat[j + 1];
				}
			}
			else
			{
				//printf(" Ken: %f", ken_cheat[n-1]);
				if (ken_cheat[n - 1] < naomi_cheat[0])
				{
					y++;
				}
				for (int j = 0; j < (n - 1); j++)
				{
					naomi_cheat[j] = naomi_cheat[j + 1];
				}
			}

		
			//}

			/*
			//Si elle a le plus haut elle le joue sinon elle triche
			if (naomi_cheat[0] < ken_cheat[0])
			{
				printf("\nNaomi: %f", naomi_cheat[0]);
			
				//Elle joue son plus léger et ne triche pas
				for (int i = 0; i < n; i++)
				{
					if (ken_cheat[i] > naomi_cheat[0])
					{
						printf(" Ken: %f", ken_cheat[i]);
						for (int j = i; j < (n - 1); j++)
						{
							ken_cheat[j] = ken_cheat[j + 1];
						}
						break;
					}
				}

				for (int j = 0; j < (n - 1); j++)
				{
					naomi_cheat[j] = naomi_cheat[j + 1];
				}
			}
			else
			{
				if (naomi_cheat[n - 1] > ken_cheat[n - 1])
				{
					printf("\nNaomi: %f", naomi_cheat[n - 1]);
					printf(" Ken: %f", ken_cheat[0]);
					y++;
					for (int j = 0; j < (n - 1); j++)
					{
						ken_cheat[j] = ken_cheat[j + 1];
					}
				}
				else
				{
					//Elle joue le plus lourd que celui qui est le plus petit de lui
					float ken_lightest = ken_cheat[0];
					float naomi_block_cheat = 0;

					for (int i = 0; i < n; i++)
					{
						if (naomi_cheat[i] > ken_lightest)
						{
							naomi_block_cheat = naomi_cheat[i];
							for (int j = i; j < (n - 1); j++)
							{
								naomi_cheat[j] = naomi_cheat[j + 1];
							}
							break;
						}
					}

					if (naomi_block_cheat != 0)
					{
						printf("\nNaomi: %f", naomi_block_cheat);
						printf(" Ken: %f", ken_cheat[0]);

						y++;
						//Ken joue son plus petit car elle annonce le poids de son plus lourd
						for (int j = 0; j < (n - 1); j++)
						{
							ken_cheat[j] = ken_cheat[j + 1];
						}
					}
					else
					{
						printf("\nNaomi: %f", naomi_cheat[0]);
						printf(" Ken: %f", ken_cheat[n - 1]);

						//Elle joue son plus léger mais annonce le plus lourd de Ken -0.0001
						for (int j = 0; j < (n - 1); j++)
						{
							naomi_cheat[j] = naomi_cheat[j + 1];
						}
					}
				}
			}
			*/
			
			n--;
		}

		printf("%d %d\n", y, z);
		
		fflush(stdout);
	}
	return 0;
}