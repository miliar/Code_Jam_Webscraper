#include<cstdio>
using namespace std;

#define N 4

char g[N+1][N+1];

char verify()
{
	int x, t, o, filled = 0;
	
	//verify rows
	for(int i=0; i<N; ++i)
	{
		x = t = o = 0;
		for(int j=0; j<N; ++j)
		{
			if(g[i][j] == 'X') ++x;
			else if(g[i][j] == 'O') ++o;
			else if(g[i][j] == 'T') ++t;
			
			if(g[i][j] != '.')
				++filled;
		}
		if(x == N || (x == N-1 && t == 1))
			return 'x';
		else if(o == N || (o == N-1 && t == 1))
			return 'o';
	}
	
	//verify cols
	for(int i=0; i<N; ++i)
	{
		x = t = o = 0;
		for(int j=0; j<N; ++j)
		{
			if(g[j][i] == 'X') ++x;
			else if(g[j][i] == 'O') ++o;
			else if(g[j][i] == 'T') ++t;
		}
		if(x == N || (x == N-1 && t == 1))
			return 'x';
		else if(o == N || (o == N-1 && t == 1))
			return 'o';
	}
	
	//verify diagonals
	x = 0, t = 0, o = 0;
	for(int i=0; i<N; ++i)
	{
		if(g[i][i] == 'X') ++x;
		else if(g[i][i] == 'O') ++o;
		else if(g[i][i] == 'T') ++t;
	}
	if(x == N || (x == N-1 && t == 1))
		return 'x';
	else if(o == N || (o == N-1 && t == 1))
		return 'o';

	x = 0, t = 0, o = 0;
	for(int i=N-1; i>=0; --i)
	{
		if(g[i][N-1 - i] == 'X') ++x;
		else if(g[i][N-1 - i] == 'O') ++o;
		else if(g[i][N-1 - i] == 'T') ++t;
	}
	if(x == N || (x == N-1 && t == 1))
		return 'x';
	else if(o == N || (o == N-1 && t == 1))
		return 'o';
	
	if(filled == N*N)
		return 'd';
	else
		return 't';
}

int main()
{
	int t;
	char line[10];
	
	gets(line);
	sscanf(line, "%d", &t);
	for(int test=1; test<=t; ++test)
	{
		for(int i=0; i<N; ++i)
			gets(g[i]);
		gets(line);
	
		char c = verify();
		printf("Case #%d: ", test);
		if(c == 'x')
			puts("X won");
		else if(c == 'o')
			puts("O won");
		else if(c == 't')
			puts("Game has not completed");
		else
			puts("Draw");
	}
		
	
	return 0;
}