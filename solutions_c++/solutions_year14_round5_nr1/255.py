#include <iostream>
#include <fstream>
#define MAXN 2000000
using namespace std;

long long arr[MAXN];
int test;
int n;
long long p, q, r, s;

ifstream fin( "A2.in" );
ofstream fout( "A2.out" );
#define cin fin
#define cout fout

void get( int& idx, long long sm ){
	long long c = 0;
	while( idx < n && c <= sm )
		c += arr[idx++];
	if( c > sm )
		idx--;
}

int main()
{
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		cin >> n >> p >> q >> r >> s;
		long long sum = 0;
		for( long long i = 0; i < n; i++ ){
			arr[i] = ( i * p + q ) % r + s;
			sum += arr[i];
		}
		long long l = 0, r = sum, res = -1;
		while( l <= r ){
			long long mid = ( l + r ) / 2;
			int idx = 0;
			for( int i = 0; i < 3; i++ )
				get( idx, mid );
			if( idx == n ){
				res = mid;
				r = mid - 1;
			}
			else l = mid + 1;
		}
		//cout << sum << ' ' << res << endl;
		double rs = (double)( sum - res ) / (double)sum;
		cout << "Case #" << T << ": ";
		cout.setf( ios::showpoint | ios::fixed );
		cout.precision( 10 );
		cout << rs << endl;
		//printf( "%.10lf\n", rs );
	}

	return 0;
}