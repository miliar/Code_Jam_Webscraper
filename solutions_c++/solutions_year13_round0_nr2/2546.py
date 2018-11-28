
#include <set>
#include <list>
#include <stack>
#include <cmath>
#include <queue>
#include <ctime>
#include <cfloat>
#include <vector>
#include <string>
#include <cstdio>
#include <bitset>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iomanip>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;


#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define RFOR(i, b, a) for(int i = b; i >= a; --i)
#define REP(i, N) for(int i = 0; i < N; ++i)
#define RREP(i, N) for(int i = N-1; i >= 0; --i)
#define FORIT(i, a) for( TI(a) i = a.begin(); i != a.end(); i++ )
#define MAXN 10000
#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3FFFFFFFFFLL
#define FILL(X, V) memset( X, V, sizeof(X) )
#define TI(X) __typeof((X).begin())
#define ALL(V) V.begin(), V.end()
#define SIZE(V) int((V).size())
#define pb push_back
#define mp make_pair

struct tri{
	int ant, novo;
	tri ( int ant = 0, int novo = 0) : ant(ant), novo(novo) { }
};

int n, m;
typedef vector < int > vi;
typedef vector < vi > vii;
typedef vector < tri > vtri;
typedef vector < vtri > vvtri;
typedef long long int64;
typedef unsigned long long uint64;

int x[] = {-1,-1,-1, 0, 1, 1, 1, 0 };
int y[] = {-1, 0, 1, 1, 1, 0,-1,-1 };

int mat[1000][1000];
vector < int > l, c;

bool solveLine(int x, int alt){
	REP(i,n) if( mat[i][x] > alt ) return false;
	return true;
}

bool solveCol(int y, int alt){
	REP(i,m) if( mat[y][i] > alt ) return false;
	return true;
}

int main(){
	ios::sync_with_stdio(false);
	int t, caso = 1;
	cin >> t;
	vector < int > nn;
	while( t-- ){
		cin >> n >> m;
		int alt = 0;
		REP(i,n){
			REP(j,m){
				cin >> mat[i][j];
				alt = max(alt, mat[i][j]);
			}			
		}
		bool ans = true;
		for( int k = alt-1; k >= 1; k--) {
			REP(i,n){ 
				REP(j,m){
					bool lin, col;
					if( mat[i][j] != k ) continue;
					lin = solveLine(j, k);
					col = solveCol(i, k);
					if( lin || col );
					else{ ans = false; break; }
				}
				if( !ans ) break;
			}
			if( !ans ) break;
		}
		cout << "Case #" << caso++ << ": " << ((ans) ? "YES" : "NO" ) << "\n";
	}
	return 0;
}
