#define _CRT_SECURE_NO_WARNINGS

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

using namespace std;


#define ASSERT(X) {if (!(X)) {printf("\n assertion failed at line %d\n",__LINE__);exit(0);}}
/*

typedef struct
{
int dist;
int length;
} vine;

vine v[10000];
int d;
int pos;
int n;
typedef pair<int, int> State;
map<State, int> dp;

int travel(int cpos, int cv)
{
State s = make_pair(cpos,cv);
if (dp.find(s) != dp.end())
{
return 0;
}
}
*/

/*
int arr1[4][4];
int arr2[4][4];
int row1;
int row2;
*/
int nbFriends = 0;
int nbAudiences = 0;
int maxShyLevel = 0;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int testcase;
	scanf("%d", &testcase);
	for (int case_id = 1; case_id <= testcase; case_id++)
	{
		nbFriends = 0;
		nbAudiences = 0;

		printf("Case #%d: ", case_id);

		scanf("%d", &maxShyLevel);
		char c;
		scanf("%c", &c);
		for (int i = 0; i <= maxShyLevel; i++)
		{
			scanf("%c", &c);
			int n = c - '0';

			if (i > nbAudiences)
			{
				nbFriends += (i - nbAudiences);
				nbAudiences += (i - nbAudiences);
			}

			nbAudiences += n;
		}


		/*
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf("%d", &arr1[i][j]);
			}
		}

		scanf("%d", &row2);
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf("%d", &arr2[i][j]);
			}
		}

		int answer;
		int nbAnswers = 0;

		//Prendre les 3 nombres de la ligne du premier arrangement et comparer combien il y en a pareil
		for (int i = 0; i < 4; i++)
		{
			int nb1 = arr1[row1 - 1][i];

			for (int j = 0; j < 4; j++)
			{
				int nb2 = arr2[row2 - 1][j];
				if (nb1 == nb2)
				{
					answer = nb1;
					nbAnswers++;
				}
			}
		}*/

		printf("%d\n", nbFriends);
		
		fflush(stdout);
	}
	return 0;
}

