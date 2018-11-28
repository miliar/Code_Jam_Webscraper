#include <stdio.h>
#include <iostream>
#include <stack>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	int caso = 0;
	scanf(" %d ", &t);
	while(t--)
	{
		caso++;
		int r1, r2;
		vector<vector<int>> cards1(4, vector<int> (4, 0)), cards2(4, vector<int> (4, 0));
		scanf(" %d ", &r1);
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				int x;
				scanf(" %d ", &x);
				cards1[i][j] = x;
			}
		}
		scanf(" %d ", &r2);
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				int x;
				scanf(" %d ", &x);
				cards2[i][j] = x;
			}
		}
		vector<int> poss;
		vector<int> final;
		for(int i = 0; i < 4; i++)
			poss.push_back(cards1[r1-1][i]);
		for(int i = 0; i < 4; i++)
			if(find( poss.begin(), poss.end(), cards2[r2-1][i]) != poss.end())
				final.push_back(cards2[r2-1][i]);
		printf("Case #%d:", caso);
		if(final.size() == 1)
			printf(" %d\n", final[0]);
		else if(final.size() == 0)
			printf(" Volunteer cheated!\n");
		else if(final.size() > 1)
			printf(" Bad magician!\n");
	}
}
