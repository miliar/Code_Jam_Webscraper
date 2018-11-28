#include <fstream>
using namespace std;

int main() {
	ifstream in;
	ofstream out;
	in.open( "A-small-attempt0.in" );
	out.open( "A-small-attempt0.out" );

	const float pi = 3.1415926535;
	int T, r, t;
	in >> T;
	
	for( int i = 1; i <= T; i++ ) {
		int s = 0, k = -2;
		in >> r >> t;

		while( s <= t )
			s += 2 * ( r + ++(++k) ) + 1;
		s -= 2 * ( r + k ) + 1;

		out << "Case #" << i << ": " << k / 2 << endl;
	}
	return 0;
}