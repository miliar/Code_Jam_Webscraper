#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <climits>
#include <queue>

using namespace std;

const double Pi=acos(-1.0);
const double Eps=1e-8;

char board[4][4+1];

char players[2+1] = "XO";
char extra = 'T';

enum outcome {X_WINS, O_WINS, DRAW, INCOMPLETE};

void printOutcome(int test, outcome out)
{
	printf("Case #%d: ", test+1);
	switch(out)
	{
		case X_WINS:
			printf("X won\n");
			break;
		case O_WINS:
			printf("O won\n");
			break;
		case DRAW:
			printf("Draw\n");
			break;
		case INCOMPLETE:
			printf("Game has not completed\n");
			break;
	}
}

int main()
{
	clock_t start = clock();
	int T;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for(int test = 0; test<T; ++test)
	{
		for(int i = 0; i<4; ++i)
			scanf("%s", board[i]);
		bool win[2] = {false, false};
		for(int p = 0; p<2; ++p)
		{
			for(int i = 0; i<4; ++i)
			{
				bool fullRow = true;
				for(int j = 0; j<4; ++j)
					if(board[i][j] != players[p] && board[i][j] != extra)
						fullRow = false;
				if(fullRow)
					win[p] = true;

				bool fullColumn = true;
				for(int j = 0; j<4; ++j)
					if(board[j][i] != players[p] && board[j][i] != extra)
						fullColumn = false;
				if(fullColumn)
					win[p] = true;
			}
			
			bool mainDiagonal = true;
			for(int i = 0; i<4; ++i)
				if(board[i][i] != players[p] && board[i][i] != extra)
					mainDiagonal = false;
			if(mainDiagonal)
				win[p] = true;

			bool antiDiagonal = true;
			for(int i = 0; i<4; ++i)
				if(board[i][3-i] != players[p] && board[i][3-i] != extra)
					antiDiagonal = false;
			if(antiDiagonal)
				win[p] = true;
		}
		
		if(win[0] && win[1])
		{
			printOutcome(test, DRAW);
			continue;
		}
		else if(win[0])
		{
			printOutcome(test, X_WINS);
			continue;
		}
		else if(win[1])
		{
			printOutcome(test, O_WINS);
			continue;
		}
		else
		{
			bool hasDot = false;
			for(int i = 0; i<4; ++i)
				for(int j = 0; j<4; ++j)
					if(board[i][j] == '.')
					{
						hasDot = true;
						break;
					}
			printOutcome(test, hasDot ? INCOMPLETE : DRAW);
		}		
	}
	fprintf(stderr, "Time elapsed: %.4lf\n", (double(clock())-start)/CLOCKS_PER_SEC);
	return 0;
}
