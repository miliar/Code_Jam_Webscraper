#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

ifstream fin( "C1.in" );
ofstream fout( "C1.out" );
#define cin fin
#define cout fout

struct hiker{
	int degSt, tm;
	hiker( int d, int t ){
		degSt = d; tm = t;
	}
	bool operator < ( const hiker& m ){
		if( degSt != m.degSt )
			return degSt < m.degSt;
		return tm < m.tm;
	}
};

vector< hiker > v;
int n;

int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		v.clear();
		cin >> n;
		for( int i = 0; i < n; i++ ){
			int d, h, m;
			cin >> d >> h >> m;
			for( int i = 0; i < h; i++ )
				v.push_back( hiker( d, m + i ) );
		}
		int res = 0;
		//cout << v[0].tm << ' ' << v[1].tm << endl;
		sort( v.begin(), v.end() );
		if( v.size() < 2 )
			res = 0;
		else{
			if( v[0].tm != v[1].tm ){
				if( v[0].tm < v[1].tm ){
					double dg = 360 - v[1].degSt;
					double tim = dg * (double)v[1].tm / 360.;
					double need = 360 - v[0].degSt + 360;
					double dd = need * v[0].tm / 360.;

					//cout << need << ' ' << dg << ' ' << dd << ' ' << tim << endl;

					if( dd - 1e-7 > tim )
						res = 0;
					else res = 1;

				}
				else{
					double dg = 360 - v[0].degSt;
					double tim = dg * v[0].tm / 360.;

					double need = 360 - v[1].degSt + 360;
					double dd = need * v[1].tm / 360.;

					

					if( dd - 1e-7 > tim )
						res = 0;
					else res = 1;
				}
			}
		}
		cout << "Case #" << T << ": " << res << endl;
	}
	return 0;
}