#include <cstdio>
#include <vector>
#include <algorithm>

int board[5][5][2];
int t,ans1,ans2;

void readBoard(int);

int main()
{
	scanf("%d", &t);
	
	for(int test = 1; test <= t; ++test)
	{
		scanf("%d", &ans1);
		readBoard(0);
		scanf("%d", &ans2);
		readBoard(1);

		std::vector<int> p;
		for(int i = 0; i < 4; ++i)
		{
			p.push_back(board[ans1-1][i][0]);
			p.push_back(board[ans2-1][i][1]);
		}

		std::sort(p.begin(),p.end());
		int No = 0, solution;

		for(int i = 1; i < p.size(); ++i)
			if(p[i] == p[i-1])
				{ No++; solution = p[i]; }
	
		if(No == 0) printf("Case #%d: Volunteer cheated!\n", test);
		else if(No > 1) printf("Case #%d: Bad magician!\n", test);
		else printf("Case #%d: %d\n", test, solution);
	}
}

void readBoard(int x)
{
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			scanf("%d", &board[i][j][x]);
}
