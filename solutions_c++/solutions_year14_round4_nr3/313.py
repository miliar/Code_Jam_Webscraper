#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <cassert>
#include <cmath>
#include <deque>
#include <map>
#include <cstring>
#include <set>

using namespace std;

typedef pair<int,int> P;
typedef long long LL;

char m[505][105];
const int dr[] = {-1,0,1,0};
const int dc[] = {0,1,0,-1};
int rows, cols;

const int N = 500*100*2+2;
class graph_t {
private:
    struct edge_t {
        int to;
        int cap;
        int flow;
        int rev_edge;
    };
    int val[N];
	vector<edge_t> edges;
    vector<int> list[N];
    int dad_edge[N];
    int n;
    std::deque<int> d;
public:
    void clear( int _n ) {
        n = _n;
		for( int i = 0; i < n; ++i ) {
			list[i].clear();
		}
		edges.clear();
    }
	void edge( int from, int to, int cap ) {
		int p_index = edges.size();
		int q_index = edges.size()+1;

		assert( from < n );
		assert( to < n );

		edge_t p, q;

		p.to = to;
		p.cap = cap;
		p.flow = 0;
		p.rev_edge = q_index;

		q.to = from;
		q.cap = cap;
		q.flow = cap;
		q.rev_edge = p_index;

		edges.push_back( p );
		edges.push_back( q );

		list[from].push_back(p_index);
		list[to].push_back(q_index);
	}
	void update_network( int from, int to, int add_flow ) {
		int b = to;

		do {
			edge_t& e = edges[dad_edge[b]];
			edge_t& e_rev = edges[e.rev_edge];
			e.flow += add_flow;
			e_rev.flow -= add_flow;
			b = e_rev.to;
		} while( b != from );
	}
	int maxflow( int from, int to ) {
		int flow = 0;

		nextpath:
			memset( val, 0, sizeof(int)*n );
			val[from] = numeric_limits<int>::max();
			dad_edge[from] = -1;
			d.clear();
			d.push_back( from );

			while( !d.empty() ) {
				int k = d.front(); d.pop_front();
				//if( k >= rows*cols ) cerr << "IN  " << k-rows*cols << ' ' << (k-rows*cols)/cols << ' ' << (k-rows*cols)%cols << endl;
				//if( k < rows*cols ) cerr << "OUT " << k << ' ' << (k)/cols << ' ' << (k)%cols << endl;

				if( k == to ) {
					flow += val[to];
					update_network( from, to, val[to] );
					goto nextpath;
				}
				for( int i = 0; i < (int)list[k].size(); ++i ) {
					edge_t& e = edges[list[k][i]];
					if( !val[e.to] && e.flow < e.cap ) {
						val[e.to] = min( val[k], e.cap - e.flow );
						dad_edge[e.to] = list[k][i];
						d.push_back( e.to );
					}
				}
			}
		return flow;
	}
};

graph_t* g = new graph_t();



inline int IN( int r, int c ) {
	return r*cols+c+rows*cols;
}

inline int OUT( int r, int c ) {
	return r*cols+c;
}


int main() {
	int cases;

	cin >> cases;

	for( int caseid = 1; caseid <= cases; ++caseid ) {
		cout << "Case #" << caseid << ": ";
		int buildings;
		cin >> cols >> rows >> buildings;
		for( int r = 0; r < rows; ++r ) {
			for( int c = 0; c < cols; ++c ) {
				m[r][c] = ' ';
			}
		}
		for( int i = 0; i < buildings; ++i ) {
			int x0, y0, x1, y1;
			cin >> x0 >> y0 >> x1 >> y1;

			int r0, c0, r1, c1;
			r1 = rows-1-y0;
			c0 = x0;

			r0 = rows-1-y1;
			c1 = x1;

			for( int r = r0; r <= r1; ++r ) {
				for( int c = c0; c <= c1; ++c ) {
					m[r][c] = '#';
				}
			}
		}

//		cerr << endl;
//		for( int r = 0; r < rows; ++r ) {
//			for( int c = 0; c < cols; ++c ) {
//				cerr << m[r][c];
//			}
//			cerr << endl;
//		}

		int src  = rows*cols*2;
		int dst = src+1;
		g->clear(dst+1);

		for( int r = 0; r < rows; ++r ) {
			for( int c = 0; c < cols; ++c ) {
				if( m[r][c] != ' ' ) continue;
				//g.edge( r*cols+c+rows*cols, r*cols+c, 1 );
				g->edge( IN(r,c), OUT(r,c), 1 );
				for( int i = 0; i < 4; ++i ) {
					int r2 = r+dr[i];
					int c2 = c+dc[i];
					if( 0 <= r2 && r2 < rows && 0 <= c2 && c2 < cols && m[r2][c2] == ' ' ) {
						//g.edge( r*cols+c, r2*cols+c2+rows*cols, 1 );
						//g.edge( r2*cols+c2, r*cols+c+rows*cols, 1 );
						//cerr << "edge " << r << ' ' << c << " -> " << r2 << ' ' << c2 << endl;
						g->edge( OUT(r,c), IN(r2,c2), 1 );
						//g.edge( OUT(r2,c2), IN(r,c), 1 );
					}
				}
			}
		}
		// connect src
		for( int c = 0; c < cols; ++c ) {
			if( m[rows-1][c] == ' ' ) {
				//g.edge( src, (rows-1)*cols+c+rows*cols, 1 );
				g->edge( src, IN(rows-1,c), 1 );
			}
		}
		// connect dst
		for( int c = 0; c < cols; ++c ) {
			if( m[0][c] == ' ' ) {
				//g.edge( 0*cols+c, dst, 1 );
				g->edge( OUT(0,c), dst, 1 );
			}
		}

		//cerr << "src/dst " << src << ' ' << dst << endl;

		int res = g->maxflow(src,dst);
		cout << res << endl;
	}
	return 0;
}
