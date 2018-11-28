#include <cstdio>
#include <algorithm>

using namespace std;

struct tire
{
	int chd[100][26], sz;

	void init()
	{
		sz = 1;
		memset(chd[0], -1, sizeof(chd[0]));
	}

	void insert( char* s )
	{
		int L = strlen(s);
		int p = 0;
		for( int i = 0; i < L; ++i )
		{
			int c = s[i] - 'A';
			if( chd[p][c] == -1 )
			{
				memset(chd[sz], -1, sizeof(chd[sz]));
				chd[p][c] = sz++;
			}
			p = chd[p][c];
		}
	}
} tir[4];

int N, M, x, y;
char s[10][20];
int id[10];
bool vis[4];

void dfs( int pos )
{
	if( pos == N )
	{
		memset(vis, 0, sizeof(vis));
		for( int i = 0; i < N; ++i )	vis[id[i]] = 1;
		for( int i = 0; i < M; ++i )	
		{
			if( !vis[i] )	return;
			tir[i].init();
		}

		for( int i = 0; i < N; ++i )
			tir[id[i]].insert(s[i]);

		int cnt = 0;
		for( int i = 0; i < M; ++i )	cnt += tir[i].sz;
		if( cnt > x )
			x = cnt, y = 1;
		else if( cnt == x )
			y++;

		return;
	}

	for( int i = 0; i < M; ++i )
	{
		id[pos] = i;
		dfs(pos+1);
	}
}

int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);

	int T, cases = 1;

	scanf("%d", &T);
	while( T-- )
	{
		scanf("%d %d", &N, &M);
		for( int i = 0; i < N; ++i )
			scanf("%s", s[i]);
		
		x = -1, y = 0;
		dfs(0);
		printf("Case #%d: %d %d\n", cases++, x, y);
	}

	return 0;
}