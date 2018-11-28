/* Google Code Jam */

#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

char winFlag;
int notCmpltd, Xwon, Owon;

int judgeGame(char* s1)
{
	for(int i=0; i<4, s1[i]=='T' || s1[i]=='X'; i++)
		if(i==3)
		{
			Xwon++;
			return 1;
		}
	for(int i=0; i<4, s1[i]=='T' || s1[i]=='O'; i++)
		if(i==3)
		{
			Owon++;
			return 1;
		}
	return 0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;

	scanf("%d", &T);

	for(int tc=1; tc<=T; tc++)
	{
		char board[4][5];
		winFlag=0;
		notCmpltd=0, Xwon=0, Owon=0;

		for(int i=0; i<4; i++)
			scanf("%s", board[i]);
/*
		for(int i=0; i<4; i++)
			printf("%s\n", board[i]);
*/
		for(int i=0; i<4; i++)
		{
			char vert[4];

			for(int j=0; j<4; j++)
				vert[j] = board[j][i];

			if(judgeGame(vert) == 1) break;

			for(int j=0; j<4; j++)
				if(board[i][j]=='.') notCmpltd++;
			if(judgeGame(board[i]) == 1) break;
		}

		char diag1[4], diag2[4];

		for(int i=0; i<4; i++)
		{
			diag1[i] = board[i][i];
			diag2[i] = board[3-i][i];
		}

		int temp = judgeGame(diag1);
		temp = judgeGame(diag2);

		if(Xwon > 0) printf("Case #%d: X won\n", tc);
		else if(Owon > 0) printf("Case #%d: O won\n", tc);
		else if(notCmpltd > 0) printf("Case #%d: Game has not completed\n", tc);
		else printf("Case #%d: Draw\n", tc);
	}

	return 0;
}