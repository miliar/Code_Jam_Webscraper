#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <deque>

using namespace std;

long T = 0;
long K = 0;
long C = 0;
long S = 0;

int main(int argc, char * argv[] )
{
	cin >> T;
	for( auto t=0; t<T; ++t )
	{
		cin >> K >> C >> S;
		cerr << K << ' ' << C << ' ' << S << ' ' << endl;
		cout << "Case #" << t+1 << ":" ;
		long step = pow( K, C - 1 );
		/*if( step < K && S < K )
		{
			cout << " IMPOSSIBLE" << endl;
			continue;
		}*/
		long r = 1;
		for( auto s=0; s<S; ++s )
		{
			cout << ' ' << r;
			r += step;
		}
		cout << endl;
	}
	return 0;
}
