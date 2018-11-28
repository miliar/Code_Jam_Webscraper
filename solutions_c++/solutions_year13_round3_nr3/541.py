#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#define P pair< long long, long long >
using namespace std;

ifstream fin( "C-small-attempt2.in" );
ofstream fout( "C1.out" );
#define cin fin
#define cout fout


struct attack{
	int tim;
	int l, r;
	int s;
	attack( int _tim, int _l, int _r, int _s ){
		tim = _tim, l = _l, r = _r, s = _s;
	}
	bool operator < ( const attack& m ){
		return tim < m.tim;
	}
};

vector< attack > v;
int test, T = 1;
int wall[30000000];
int n;
int CONS = 10000;

int main(){
	for( cin >> test; test--; ){
		v.clear();
		memset( wall, 0, sizeof wall );
		cin >> n;
		for( int i = 0; i < n; i++ ){
			int di, ni, li, ri, si, delta_di, delta_pi, delta_si;
			cin >> di >> ni >> li >> ri >> si >> delta_di >> delta_pi >> delta_si;
			for( int j = 0; j < ni; j++ ){
				v.push_back( attack( di, li, ri, si ) );
				di += delta_di;
				si += delta_si;
				li += delta_pi;
				ri += delta_pi;
			}
		}
		sort( v.begin(), v.end() );
		int suc = 0;
		for( int i = 0; i < v.size(); i++ ){
			
			int j = i;
			while( j < v.size() && v[j].tim == v[i].tim )
				j++;
			for( int k = i; k < j; k++ ){
				bool sc = 1;
				for( int z = v[k].l + CONS; z < v[k].r + CONS; z++ )
					if( wall[z] < v[k].s )
						sc = 0;
				//cout << "HERE " << i << ' ' << sc << endl;
				if( !sc )
					suc++;
			}
			//cerr << i << ' ' << j << endl;
			for( int k = i; k < j; k++ ){
				for( int z = v[k].l + CONS; z < v[k].r + CONS; z++ )
					wall[z] = max( wall[z], v[k].s );
			}
			i = j - 1;
		}
		//cerr << test << endl;
		cout << "Case #" << T++ << ": ";
		cout << suc << endl;
	}
	return 0;
}