#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char board[64][64];
int R, C, M;
int dx[8] = {-1, 0,+1,-1,+1,-1, 0,+1}; 
int dy[8] = {-1,-1,-1, 0, 0,+1,+1,+1};
int mrc[64][64];
int marcados;

void dfs(int i, int j)
{
	mrc[i][j] = 1;
	marcados++;
	for(int k = 0; k < 8; k++)
	{
		int ii = i + dx[k];
		int jj = j + dy[k];
		if( ii < 0 or jj < 0 or ii >= R or jj >= C) continue;
		if( board[ii][jj] == '*') return;
	}
	for(int k = 0; k < 8; k++)
	{
		int ii = i + dx[k];
		int jj = j + dy[k];
		if( ii < 0 or jj < 0 or ii >= R or jj >= C) continue;
		if( mrc[ii][jj] == 0)
		{
			dfs(ii,jj);
		}
	}
}


void printBoard()
{
	for(int i = 0; i < R;i++)
	{
		for(int j = 0; j < C;j++)
		{
			printf("%c", board[i][j]);
		}
		printf("\n");
	}
}


bool isPossible(int num)
{
	memset(board, '.', sizeof board);
	for(int i = 0; i < R; i++)
	{
		for(int j = 0; j < C; j++)
		{
			int tmp = i*C + j;
			if( (num & (1<<tmp)) > 0) board[i][j] = '*';
		}
	}
	//printf("teste\n");
	//printBoard();
	//printf("endteste\n");
	for(int i = 0; i < R; i++)
	{
		for(int j = 0; j < C; j++)
		{
			if( board[i][j] == '.')
			{
				memset(mrc,0,sizeof(mrc));
				marcados = M;
				board[i][j] = 'c';
				dfs(i,j);
				if( marcados == R*C) return true;
				board[i][j] = '.';
			}
		}
	}
	return false;
}

int main() {
	// your code goes here
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <=t; tc++)
	{
		scanf("%d%d%d", &R, &C, &M);
		printf("Case #%d:\n", tc);
		bool ok = false;
		for(int i = 0; i < 1<<(R*C); i++)
		{
			int cnt = 0;
			for(int j = 0; j < (R*C); j++)
			{
				if( (i & (1<<j)) > 0 ) cnt++;
			}
			if (cnt == M)
			{
				if( isPossible(i) )
				{
					printBoard();
					ok = true;
					break;
				}
			}
		}
		if( ok == false)
		{
			puts("Impossible");
		}
		
	}
	return 0;
}
