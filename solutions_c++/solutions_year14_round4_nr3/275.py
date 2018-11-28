#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cassert>
#include <cstring>
#include <sstream>
#include <ext/numeric>
#include <gmpxx.h>			// -lgmpxx -lgmp
using namespace std ;
using namespace __gnu_cxx ;
typedef mpz_class BIGNUM ;
typedef long long LL ;
typedef pair<int,int> PII ;
typedef vector<int> VI ;
const int INF = 1000*1000*1000 ;
const LL INFLL = (LL)INF * (LL)INF ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define CLEAR(t) memset(t,0,sizeof(t))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

template<class T1, class T2> ostream & operator<<(ostream &s, pair<T1,T2> x) { s << "(" << x.FI << "," << x.SE << ")" ; return s ; }
template<class T> ostream & operator<<(ostream &s, const vector<T> &t) { FOREACH(it, t) s << *it << " " ; return s ; }
template<class T1, class T2> ostream & operator<<(ostream &s, const map<T1, T2> &t) { FOREACH(it, t) s << *it << " " ; return s ; }

const int MAXW = 110 ;
const int MAXH = 510 ;
bool board[MAXW][MAXH] ;
const int MAXSIZE = 2*MAXW*MAXH ;

//////////////////////////////////////////////////
VI graf[MAXSIZE] ;
bool visited[MAXSIZE] ;
int S, T ;
vector<int> path ;

// szuka sciezki powiekszajacej za pomoca DFS
bool isPath(int u) {
	path.PB(u) ;
	visited[u] = true ;
	if(u==T) return true ;
	FOREACH(i, graf[u]) {
		if(!visited[*i]) {
			if(isPath(*i)) return true ;
		}
	}		// .. not found
	path.pop_back() ;
	return false ;
}

void revEdge(int a, int b) {
	int i ;
	bool found=false ;
	REP(i, graf[a].size()) {
		if(graf[a][i]==b) {
			swap(graf[a][i], graf[a].back()) ;
			graf[a].pop_back() ;
			found=true ;
			break ;
		}
	}
	assert(found) ;
	graf[b].PB(a) ;
}

int maxFlow(int S, int T) {
	::S=S ;		// wierzcholek poczatkowy
	::T=T ;	// wierzcholek koncowy
	CLEAR(visited) ;
	path.clear() ;
	while(isPath(S)) {
		for(int i=0 ; i+1<path.size() ; i++) {
			int a = path[i], b = path[i+1] ;
			revEdge(a,b) ;
		}
		CLEAR(visited) ;
		path.clear() ;
	}
	return graf[T].size() ;
}
///////////////////////////////////////////

int W, H ;

int index(int i, int j, bool end) {
	return 2*(j*W+i)+1+end ;
}
bool can(int i, int j) {
	return i>=0 && i<W && j>=0 && j<H && !board[i][j] ;
}

void link(int a, int b) {
	graf[a].PB(b) ;
}

void _main() {
	CLEAR(board) ;
	int i, j, k, b, x0, y0, x1, y1 ;
	REP(i,MAXSIZE) graf[i].clear() ;
	
	cin >> W >> H >> b ;
//	cout << "W="<< W<< " H="<< H << " b=" << b << endl ;
	while(b--) {
		cin >> x0 >> y0 >> x1 >> y1 ;
		for(i=x0 ; i<=x1 ; i++)
			for(j=y0 ; j<=y1 ; j++)
				board[i][j] = true ;
	}
	int S=0, T=index(W-1,H-1,1)+1 ;
//	cout << "S=" << S << " T=" << T << endl ;
	REP(i,W) {
		if(can(i,0))
			link(S, index(i,0,0)) ;
		if(can(i,H-1))
			link(index(i,H-1,1), T) ;
	}
	int add_x[4]={0,0,-1,1} ;
	int add_y[4]={-1,1,0,0} ;
	REP(i,W)
		REP(j,H) {
			if(!can(i,j)) continue ;
			link(index(i,j,0),index(i,j,1)) ;
			REP(k,4) {
				int ni = i+add_x[k] ;
				int nj = j+add_y[k] ;
				if(!can(ni,nj)) continue ;
				link(index(i,j,1),index(ni,nj,0)) ;
			}
		}
	
	cout << maxFlow(S,T) << endl ;
}

int main()
{
	ios_base::sync_with_stdio(0) ;
	int C ;
	cin >> C ;
	for(int tests=1 ; tests<=C ; tests++) {
		cerr << "Case #" << tests << endl ;
		cout << "Case #" << tests << ": " ;
		_main() ;
	}
}

