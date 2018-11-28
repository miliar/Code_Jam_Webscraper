#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#define EPS 1e-7
#define pdd pair< double, double >

using namespace std;

ifstream fin( "B1.in" );
ofstream fout( "B111.out" );
#define cin fin
#define cout fout

bool cmp1( pdd p1, pdd p2 ){
	if( p1.first == p2.first )
		return p1.second > p2.second;
	return p1.first < p2.first;
}

bool cmp2( pdd p1, pdd p2 ){
	if( p1.first == p2.first )
		return p1.second > p2.second;
	return p1.first > p2.first;
}

vector< pdd > so;
vector< pdd > rso;
double V, X;
int n;

double get( vector< pdd >& w, double T ){
	double rem = V;
	double soor = 0;
	for( int i = 0; i < w.size(); i++ ){
		double now = T * w[i].second;
		soor += min( now, rem ) * w[i].first;
		rem -= min( now, rem );
	}
	if( rem - EPS > 0 )
		return -1;
	return soor / V;
}

int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		so.clear();
		rso.clear();
		cin >> n >> V >> X;
		for( int i = 0; i < n; i++ ){
			double r, c;
			cin >> r >> c;
			so.push_back( pdd( c, r ) );
			rso.push_back( pdd( c, r ) );
		}
		cout << "Case #" << T << ": ";
		if( n == 1 ){
			cout.setf( ios::showpoint | ios::fixed );
			cout.precision( 7 );
			if( X == so[0].first )
				cout << V / so[0].second << endl;
			else cout << "IMPOSSIBLE" << endl;
		}
		else{
			cout.setf( ios::showpoint | ios::fixed );
			cout.precision( 7 );
			if( so[0].first == so[1].first ) {
				if( X == so[0].first )
					cout << V / ( so[0].second + so[1].second ) << endl;
				else cout << "IMPOSSIBLE" << endl;
			}
			else{
				double v0 = V * ( X - so[1].first ) / ( so[0].first - so[1].first );
				double v1 = V - v0;
				if( v0 + EPS < 0 || v1 + EPS < 0 )
					cout << "IMPOSSIBLE" << endl;
				else cout << max( v0 / so[0].second, v1 / so[1].second ) << endl;
			}
		}
		/*sort( so.begin(), so.end(), cmp1 );
		sort( rso.begin(), rso.end(), cmp2 );
		double l = 0, r = 1e9;
		for( int iter = 0; iter < 1000; iter++ ){
			double mid = ( l + r ) / 2;
			double mn = get( so, mid );
			double mx = get( rso, mid );
			if( mn == -1 || mx == -1 )
				l = mid;
			else{
				if( X >= mn && X <= mx )
					r = mid;
				else l = mid;
			}
		}
		cout << "Case #" << T << ": ";
		if( l >= 1e9 - EPS )
			cout << "IMPOSSIBLE" << endl;
		else{
			cout.setf( ios::showpoint | ios::fixed );
			cout.precision( 7 );
			cout << l << endl;
		}*/
	}

	return 0;
}