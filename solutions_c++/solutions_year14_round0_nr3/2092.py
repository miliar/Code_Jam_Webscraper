#include <cstdio>
#include <cstring>
#include <queue>
#include <utility>
#include <algorithm>
using namespace std;

int R, C, M;
char board[5][5];

typedef pair<int,int> ii;
bool validate() {
	
	
	bool visited[5][5];
	bool deadend[5][5];
	memset(deadend,0,sizeof(deadend));
	for( int i = 0 ; i < R ; ++i ) for( int j = 0 ; j < C ; ++j ) if( board[i][j] == '*' ) {
		for( int di = -1 ; di <= 1 ; ++di ) for( int dj = -1 ; dj <= 1 ; ++dj ) {
			if( ! di && ! dj ) continue;
			if( i + di < 0 || i + di >= R ) continue;
			if( j + dj < 0 || j + dj >= C ) continue;
			if( board[i+di][j+dj] == '.' ) {
				deadend[i+di][j+dj] = true;
			}
		}
	}

	const int di[] = { -1, 1, 0, 0 };
	const int dj[] = { 0, 0, -1, 1 };
	for( int i = 0 ; i < R ; ++i ) for( int j = 0 ; j < C ; ++j ) if( board[i][j] == '.' ) {

		memset( visited, 0, sizeof visited );
		queue<ii> que;
		que.push( ii(i,j) );

		int nempty = 0;
		visited[i][j] = true;
		while( !que.empty() ) {
			ii top = que.front();
			que.pop();
			int ci = top.first;
			int cj = top.second;
			++nempty;
			if( deadend[ci][cj] ) continue;
			for( int di = -1 ; di <= 1 ; ++di ) for( int dj = -1 ; dj <= 1 ; ++dj ) {
				if( !di && !dj ) continue;
				int nexti = ci + di;
				int nextj = cj + dj;
				if( nexti < 0 || nexti >= R ) continue;
				if( nextj < 0 || nextj >= C ) continue;
				if( visited[nexti][nextj] ) continue;
				if( board[nexti][nextj] == '.' ) {
					que.push(ii(nexti,nextj));
					visited[nexti][nextj] = true;
				}
			}
		}	
	
		if( nempty == R * C - M ) {
			board[i][j] = 'c';
			for( int k = 0 ; k < R ; ++k ) {
				for( int l = 0 ; l < C ; ++l ) {
					printf("%c", board[k][l]);
				}
				printf("\n");
			}
			return true;
		}
	}

	return false;
}

bool solve( int i, int j, int remain ) {
	
	if( j == C ) {
		return solve(i+1,0,remain);
	}
	if( i >= R ) {
		if( remain == 0 ) return validate();
		else return false;
	}

	if( remain > 0 ) {
		board[i][j] = '*';
		if( solve(i,j+1,remain-1) ) {
			return true;
		}
	}
	board[i][j] = '.';
	if( solve(i,j+1,remain) ) {
		return true;
	}
	return false;
}

int main() {
	int ncase;
	scanf("%d", &ncase);
	
	for( int caseno = 1 ; caseno <= ncase ; ++caseno ) {
		scanf("%d %d %d", &R, &C, &M);
		printf("Case #%d:\n", caseno);
		bool ret = solve( 0, 0, M );
		if( !ret ) printf("Impossible\n");
	}
	return 0;
}
