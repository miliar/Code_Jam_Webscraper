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

string sorting ( string str )
{
	if( str.size() == 2 ){
		sort(all(str));
		return str;
	}

	string str1 = str.substr(0, str.size()/2), str2 = str.substr(str.size()/2, str.size()/2);
	return min(sorting(str2) + sorting(str1), sorting(str1) + sorting(str2)); 
}

pair<bool,string> solve ( int r, int p, int s, string str )
{
	if( r == 0 && p == 0 && s == 0 ){
		return mp(true, sorting(str));
	}
	
	string n_str = "";
	rep(i, str.size()){
		if( str[i] == 'R' ){
			if( s > 0 ){ n_str += "RS"; --s; }
			else return mp(false, "IMPOSSIBLE");
		}			
		if( str[i] == 'P' ){
			if( r > 0 ){ n_str += "PR"; --r; }
			else return mp(false, "IMPOSSIBLE");
		}			
		if( str[i] == 'S' ){
			if( p > 0 ){ n_str += "SP"; --p; }
			else return mp(false, "IMPOSSIBLE");
		}
	}
	
	return solve(r, p, s, n_str);
}

int main()
{
	int T;
	cin >> T;

	rep(n, T){
		int N;
		int r,p,s;
		cin >> N;
		cin >> r >> p >> s;

		string ans = "Z";
		pair<bool, string> ret;
		ret = solve(r-1, p, s-1, "RS");
		if( ret.fs ) ans = min(ans, ret.sc);
		ret = solve(r-1, p-1, s, "PR");
		if( ret.fs ) ans = min(ans, ret.sc);
		ret = solve(r, p-1, s-1, "SP");
		if( ret.fs ) ans = min(ans, ret.sc);

		if( ans == "Z" ) ans = "IMPOSSIBLE";

		cout << "Case #" << n+1 << ": " << ans << endl;
	}
}
