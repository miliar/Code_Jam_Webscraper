#include <bits/stdc++.h>
using namespace std;

struct NEdge {
	int to, cap, invId;
	NEdge ( int to, int cap, int invId ) :
		to(to), cap(cap), invId(invId) { }
	NEdge ( ) { }
};

struct Network
{
	int n, src, snk;
	vector<vector<NEdge> > out;
	vector<int> prv;

	void pushFlow ( int a, int b ) {
		for ( int i = 0; ; ++i )
			if ( out[a][i].to == b ) {
				out[a][i].cap--;
				out[ out[a][i].to ][ out[a][i].invId ].cap++;
				return;
			}
	}

	bool augment ( )
	{
		fill ( prv.begin(), prv.end(), -1 );

		queue<int> q;
		prv[src] = src;
		q.push ( src );
		while ( !q.empty() )
		{
			int cur = q.front();
			q.pop();

			for ( int i = 0; i < int(out[cur].size()); ++i )
			{
				if ( prv[out[cur][i].to] != -1 ) continue;
				if ( out[cur][i].cap == 0 ) continue;
				prv[out[cur][i].to] = cur;
				q.push ( out[cur][i].to );
			}
		}

		if ( prv[snk] == -1 )
			return false;

		for ( int i = snk; i != src; i = prv[i] )
			pushFlow ( prv[i], i );

		return true;
	}

	int maxFlow ( ) {
		int ans = 0;
		while ( augment() ) ans++;
		return ans;
	}

	void addEdge ( int fr, int to, int cap ) {
		out[fr].push_back ( NEdge(to,cap,int(out[to].size())) );
		out[to].push_back ( NEdge(fr,0,int(out[fr].size())-1) );
	}

	Network ( int nNodes, int source, int sink ) {
		n=nNodes; src=source; snk=sink;
		out.assign ( n, vector<NEdge>() );
		prv.resize ( n );
	}
};

const int di[] = { 0, 0, -1, 1 };
const int dj[] = { -1, 1, 0, 0 };
int h, w;

int encodeIn ( int i, int j ) { return 2*(j+i*w); }
int encodeOut ( int i, int j ) { return 2*(j+i*w)+1; }

bool valid ( int i, int j ) {
	return 0 <= i && 0 <= j && i < h && j < w;
}

int main ( )
{
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int nTests;
	cin >> nTests;

	for ( int curT = 1; curT <= nTests; ++curT )
	{
		int nBlocks;
		cin >> w >> h >> nBlocks;
		vector<vector<bool> > mat ( h, vector<bool> ( w, true ) );
		while ( nBlocks-- )
		{
			int si, sj, bi, bj;
			cin >> sj >> si >> bj >> bi;
			for ( int i = si; i <= bi; ++i )
				for ( int j = sj; j <= bj; ++j )
					mat[i][j] = false;
		}

		Network G ( 2*h*w+2, 2*h*w, 2*h*w+1 );
		for ( int i=0, ni; i < h; ++i )
			for ( int j=0, nj; j < w; ++j ) {
				if ( !mat[i][j] ) continue;
				for ( int d = 0; d < 4; ++d ) {
					ni=i+di[d]; nj=j+dj[d];
					if ( !valid(ni,nj) ) continue;
					if ( !mat[ni][nj] ) continue;
					G.addEdge ( encodeOut(i,j), encodeIn(ni,nj), 1 );
				}
			}

		for ( int i = 0; i < h; ++i )
			for ( int j = 0; j < w; ++j )
				G.addEdge ( encodeIn(i,j), encodeOut(i,j), 1 );

		for ( int j = 0; j < w; ++j ) {
			G.addEdge ( G.src, encodeIn(0,j), 1 );
			G.addEdge ( encodeOut(h-1,j), G.snk, 1 );
		}
		
		cout << "Case #" << curT << ": " << G.maxFlow() << '\n';
	}

	return 0;
}
