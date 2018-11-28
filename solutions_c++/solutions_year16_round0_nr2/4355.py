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

int main()
{
	int T;
	cin >> T;
	
	rep(n, T){
		string s, S;
		cin >> s;
		S = s;
		
		int ans1 = 0, idx = s.size();
		while(idx > 0){
			if( s[idx-1] == '+' ){
				--idx;
				continue;
			}
			if( s[0] == '-' ){
				++ans1;
				string s1 = s.substr(0, idx), s2 = "";
				rep(i, s1.size()) s2 += (s1[s1.size()-i-1] == '+' ? '-' : '+');
				s = s2 + s.substr(idx);
				--idx;
			}
			else{
				++ans1;
				s[0] = '-';
			}
		}

		s = S;
		idx = 0;
		int ans2 = 0;
		while( idx < s.size() ){
			bool flag = true;
			rep(i, s.size()) if( s[i] == '-' ){ flag = false; break; }
			if( flag ) break;

			int prev_idx = idx;
			while( idx < s.size() && s[idx] == '+' ) ++idx;
			if( idx != prev_idx ){
				rep(i, idx) s[i] = '-';
				++ans2;
			}
			
			prev_idx = idx;
			while( idx < s.size() && s[idx] == '-' ) ++idx;
			if( idx != prev_idx ){
				rep(i, idx) s[i] = '+';
				++ans2;
			}
		}
		cout << "Case #" << n+1 << ": " << min(ans1, ans2) << endl;
	}
}
