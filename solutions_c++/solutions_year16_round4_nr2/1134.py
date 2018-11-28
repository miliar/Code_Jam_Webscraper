// Standard I/O
#include <iostream>
#include <sstream>
#include <cstdio>
// Standard Library
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
// Template Class
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
// Container Control
#include <algorithm>

using namespace std;

#define rep( i, n ) for( int i = 0; i < n; ++i )
#define irep( i, n ) for( int i = n-1; i >= 0; --i )
#define reep( i, s, n ) for ( int i = s; i < n; ++i )
#define ireep( i, n, s ) for ( int i = n-1; i >= s; --i )
#define foreach(itr, x) for( typeof(x.begin()) itr = x.begin(); itr != x.end(); ++itr)

#define mp make_pair
#define pb push_back
#define eb emplace_back
#define all( v ) v.begin(), v.end()
#define fs first
#define sc second
#define vc vector

// for visualizer.html
double SCALE = 1.0;
double OFFSET_X = 0.0;
double OFFSET_Y = 0.0;
#define LINE(x,y,a,b) cerr << "line(" << SCALE*(x) + OFFSET_X << ","	\
	<< SCALE*(y) + OFFSET_Y << ","										\
	<< SCALE*(a) + OFFSET_X << ","										\
	<< SCALE*(b) + OFFSET_Y << ")" << endl;
#define CIRCLE(x,y,r) cerr << "circle(" << SCALE*(x) + OFFSET_X << ","	\
	<< SCALE*(y) + OFFSET_Y << ","										\
	<< SCALE*(r) << ")" << endl;

typedef long long ll;
typedef complex<double> Point;

typedef pair<int, int> pii;
typedef pair<int, pii> ipii;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector< vector<int> > vii;
typedef vector< vector<double> > vdd;

typedef vector<int>::iterator vi_itr;

const int IINF = 1 << 28;
const double INF = 1e30;
const double EPS = 1e-10;
const double PI = acos(-1.0);

// Direction : L U R D
const int dx[] = { -1, 0, 1, 0};
const int dy[] = { 0, -1, 0, 1 };

double p[200] = { 0.0 };
int N, K;

double solve1 ( vi idx )
{
	double ans = 0.0;
	rep(i, (1 << K)){
		if( __builtin_popcount(i) == K/2 ){
			double tmp = 1.0;
			rep(j, K){
				if( (i & (1 << j)) != 0 ) tmp *= p[idx[j]];
				else tmp *= 1.0 - p[idx[j]];
			}
			ans += tmp;
		}
	}

	return ans;
}

double solve2 ( int depth, int k, vi idx )
{
	if( k == 0 ){
		return solve1(idx);
	}
	if( depth == N ) return 0.0;

	double ret = 0.0;
	ret = solve2( depth+1, k, idx );
	idx.pb(depth);
	ret = max(ret, solve2(depth+1, k-1, idx));

	return ret;
}

int main()
{
	int T;
	cin >> T;
	
	rep(n, T){

		double ans = 0.0;
		cin >> N >> K;
		rep(i, N) cin >> p[i];

		ans = solve2(0, K, vi());

		printf("Case #%d: %.10f\n", n+1, ans);
	}
}
