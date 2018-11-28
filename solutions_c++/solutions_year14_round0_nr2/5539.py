#include <iostream>
#include <fstream>

using namespace std;

ifstream fin( "B2.in" );
ofstream fout( "B2.out" );
#define cin fin
#define cout fout

int T;
double c, f, x;

int main()
{
	cin >> T;
	for( int tt = 1; tt <= T; tt++ ){
		cerr << tt << endl;
		cin >> c >> f >> x;
		double cf = 2., sum = 0;
		double ret = 1e9;
		for( int rep = 0; rep < 100000000; rep++ ){
			ret = min( ret, sum + x / cf );
			sum += c / cf;
			cf += f;
		}
		cout << "Case #" << tt << ": ";
		cout.setf( ios::showpoint | ios::fixed );
		cout.precision( 7 );
		cout << ret << endl;
		//printf( "%.7lf\n", ret );
	}
	return 0;
}