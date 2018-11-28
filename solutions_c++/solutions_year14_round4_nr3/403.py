#include <iostream>
#include <vector>
#define MAXV 1000007
#define pii pair< int, int >
#define INF 1000000000
#include <fstream>
#pragma comment(linker, "/STACK:50000000") 

using namespace std;

ifstream fin( "C1.in" );
ofstream fout( "C1.out" );
#define cin fin
#define cout fout

vector< int > adj[MAXV], rev[MAXV], cap[MAXV];
pii path[MAXV];
int ptr = 0;
bool mark[MAXV];

void addEdge( int v1, int v2, int capacity ){
	adj[v1].push_back( v2 );
	adj[v2].push_back( v1 );
	rev[v1].push_back( adj[v2].size() - 1 );
	rev[v2].push_back( adj[v1].size() - 1 );
	cap[v1].push_back( capacity );
	cap[v2].push_back( 0 );
}

int dfs( int cur, int tar, int minCap ){
	mark[cur] = true;
	if( cur == tar )
		return minCap;
	for( int i = 0; i < adj[cur].size(); i++ ){
		int next = adj[cur][i];
		if( mark[next] || !cap[cur][i] )
			continue;
		path[ptr++] = pii( cur, i );
		int df = dfs( next, tar, min( minCap, cap[cur][i] ) );
		if( df )
			return df;
		ptr--;
	}
	return 0;
}

int maxFlow( int so, int tar ){
	int flow = 0;
	ptr = 0;
	memset( mark, false, sizeof mark );
	while( true ){
		int curFlow = dfs( so, tar, INF );
		if( curFlow == 0 )
			break;
		flow += curFlow;
		for( int i = 0; i < ptr; i++ ){
			int ver = path[i].first;
			int id = path[i].second;
			cap[ver][id] -= curFlow;
			cap[adj[ver][id]][rev[ver][id]] += curFlow;
		}
		ptr = 0;
		memset( mark, false, sizeof mark );
	}
	return flow;
}

void clearFlow(){
	for( int i = 0; i < MAXV; i++ )
		adj[i].clear(), rev[i].clear(), cap[i].clear();
}

int test;
bool inv[1000][1000];

// W for x
// H for y 

int W, H, B;

inline int in( int x, int y ){
	return 2 * ( y * W + x );
}

inline int out( int x, int y ){
	return 2 * ( y * W + x ) + 1;
}

int dr[4][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int main()
{
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		cerr << T << endl;
		clearFlow();
		memset( inv, false, sizeof inv );
		cin >> W >> H >> B;
		for( int i = 0; i < B; i++ ){
			int X[2], Y[2];
			for( int j = 0; j < 2; j++ )
				cin >> X[j] >> Y[j];
			for( int x = X[0]; x <= X[1]; x++ )
				for( int y = Y[0]; y <= Y[1]; y++ )
					inv[x][y] = true;
		}
		int so = 2 * W * H + 5;
		int tar = so + 1;
		for( int x = 0; x < W; x++ )
			for( int y = 0; y < H; y++ ){
				//cout << x << ' ' << y << ' ' << inv[x][y] << endl;
				if( inv[x][y] == true )
					continue;
				
				if( y == 0 )
					addEdge( so, in( x, y ), 1 );
				if( y == H - 1 )
					addEdge( out( x, y ), tar, 1 );
				addEdge( in( x, y ), out( x, y ), 1 );
				for( int k = 0; k < 4; k++ ){
					int nx = x + dr[k][0];
					int ny = y + dr[k][1];
					if( nx >= 0 && nx < W && ny >= 0 && ny < H && inv[nx][ny] == false )
						addEdge( out( x, y ), in( nx, ny ), 1 );
				}
			}
		cerr << "DSDS " << endl;
		cout << "Case #" << T << ": " << maxFlow( so, tar ) << endl;
		cerr << "DSDSD " << endl;
	}

	return 0;
}