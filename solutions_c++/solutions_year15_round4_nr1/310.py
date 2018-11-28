#include <stdio.h>
#include <string.h>
#include <assert.h>

char maps[200][200];
int crow[200];
int ccol[200];
int U[200], D[200], L[200], R[200];
int r, c;

bool check()
{
	for(int i = 0; i < r; ++i)
		for(int j = 0; j < c; ++j)
			if(crow[i] == 1 && ccol[j] == 1 && maps[i][j] != '.')
				return true;
	return false;
}
bool pos(int i, int j)
{
	assert(i >= U[j] && i <= D[j] && j >= L[i] && j <= R[i]);
	if(i == U[j] && maps[i][j] == '^') return true;
	if(i == D[j] && maps[i][j] == 'v') return true;
	if(j == L[i] && maps[i][j] == '<') return true;
	if(j == R[i] && maps[i][j] == '>') return true;
	return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int ca = 1; ca <= T; ++ca)
	{
		scanf("%d %d", &r, &c);
		for(int i = 0; i < r; ++i)
			scanf("%s", maps[i]);
		memset(crow, 0, sizeof(crow) );
		memset(ccol, 0, sizeof(ccol) );
		memset(U, 0xff, sizeof(U) );
		memset(D, 0xff, sizeof(D) );
		memset(L, 0xff, sizeof(L) );
		memset(R, 0xff, sizeof(R) );
		for(int i = 0; i < r; ++i)
		{
			for(int j = 0; j < c; ++j)
			{
				if(maps[i][j] != '.')
				{
					++crow[i];
					++ccol[j];

					if(U[j] == -1 || i < U[j]) U[j] = i;
					if(D[j] == -1 || i > D[j]) D[j] = i;
					if(L[i] == -1 || j < L[i]) L[i] = j;
					if(R[i] == -1 || j > R[i]) R[i] = j;
				}
			}
		}
		bool impossible = check();
		int cnt = 0;
		for(int i = 0; i < r; ++i)
		{
			for(int j = 0; j < c; ++j)
			{
				if( maps[i][j] != '.' && pos(i,j) )
					++cnt;
			}
		}
		printf("Case #%d: ", ca);
		if(impossible)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", cnt);
	}
}
