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

bool isprime[100000001];
int main()
{
	int T;
	cin >> T;

	rep(i, 100000001) isprime[i] = true;
	isprime[0] = isprime[1] = false;
	reep(i, 2, 100000001){
		if( isprime[i] ){
			for( int j = 2*i; j < 100000001; j+=i ){
				isprime[j] = false;
			}
		}
	}
	
	rep(n, T){
		int N, J;
		cin >> N >> J;

		long long ten_pow = 1;
		rep(i, N-1) ten_pow *= 10;
		
		cout << "Case #" << n+1 << ":" << endl;
		int cnt = 0;
		for( long long i = 0; i < (1ll << N-2); ++i ){
			bool isok = false;
			long long M = 0;
			long long divid[16] = { 0 };

			rep(k, N-2){
				M = 10*M + ((i&(1ll << k)) ? 1 : 0);
			}
			M = ten_pow + 10*M + 1;

			reep(j, 2, 11){
				long long num = 0;
				long long tmp = M, base = 1;
				
				while( tmp > 0 ){
					num += base * (tmp % 10);
					base *= j;
					tmp /= 10;
				}

				for( long long k = 2; k*k < num; ++k ){
					if( isprime[k] && num%k == 0 ){
						divid[j] = k;
						break;
					}
				}

				if( divid[j] == 0 ){
					isok = true;
					break;
				}

			}

			if( !isok ){
				cout << M;
				reep(j, 2, 11) cout << " " << divid[j];
				cout << endl;
				++cnt;
			}
			if( cnt == J ) break;
		}
	}
}
