#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define fori(i, n) for ( int i = 0; i < (n); ++i )
#define forr(i, a, b) for ( int i = (a); i <= (b); ++i )
#define ford(i, a, b) for ( int i = (a); i >= (b); --i )
#define tr(it, a, b) for ( typeof(a) it = (a); it != (b); ++it )
#define all(x) (x).begin(),(x).end()
#define sz size()
#define pb push_back

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }
template<class T> T s2a(string s) { istringstream i(s); T x; i >> x; return x; }

const double EPS = 1e-9;
const int INF = 0x3F3F3F3F;

int cmpD( double x, double y = 0, double tol = EPS )
{
    return ( x <= y + tol ) ? ( x + tol < y ) ? -1 : 0 : 1;
}

bool check( int h, pair< int, int > p, const vector< vector< int > > & mat )
{
	int i = p.first, j = p.second;
	bool ok_line = true, ok_column = true;

	// check line
	fori(k,mat[i].sz) if ( mat[i][k] > h )
	{
		ok_line = false;
		break;
	}

	// check column
	fori(k,mat.sz) if ( mat[k][j] > h )
	{
		ok_column = false;
		break;
	}

	return ok_line || ok_column;
}

int main()
{
	ios::sync_with_stdio(false);
	int T, n, m;
	bool ok;
	cin >> T;
	forr(t,1,T)
	{
		ok = true;
		cin >> n >> m;
		vector< vector< int > > mat(n, vector< int >(m));
		vector< vector< pair< int, int > > > v(101); 
		fori(i,n) fori(j,m) 
		{
			cin >> mat[i][j];
			v[mat[i][j]].push_back( make_pair(i,j) );
		}
		forr(h,1,100) fori(j,v[h].sz) 
		{
			// cout << h << " " << v[h][j].first << " " << v[h][j].second << endl;
			if( !check(h, v[h][j], mat) )
			{
				ok = false;
				break;
			}
		}
		cout << "Case #" << t << ": " << (ok ? "YES" : "NO") << endl;
	}
    return 0;
}
