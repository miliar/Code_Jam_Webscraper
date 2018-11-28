#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <float.h>
#include <iomanip>
#include <ctime>
#include <stack>
#include <limits>
//#define FOR( i, N ) for( int (i) = 0; (i) < (N); (i)++ )
//#define FOR_( i, start, endplusone ) for( int (i) = (start); (i) < (endplusone); (i)++ )
const double EPS = 1e-10;
const double PI = 3.141592653589793;
using namespace std;
//#define ull unsigned long long
int compare( const void * a, const void * b ){
	return ( *(int*)a - *(int*)b );
}
int main(){
	//ifstream ifs( "A-small-attempt1.in" );
	//ifstream ifs( "A-sample.in" );
	ifstream ifs( "A-large.in" );
	int T, N, X;
	const int Nmax = 10000;
	int S[Nmax] = {};
	ifs >> T;
	ofstream ofs( "out" );
	for( int i = 1; i <= T; i++ ){
		ifs >> N >> X;
		for( int j = 0; j < N; j++ ){
			ifs >> S[j];
		}
		qsort( S, N, sizeof(S[0]), compare );
		//algorithm
		int p = 0, q = N-1, cnt = 0;
		while( q >= p ){
			cnt++;
			if( S[p] + S[q] <= X ){
				p++;
				q--;
			}else{
				q--;
			}
		}
		ofs << "Case #" << i << ": " << cnt << endl;
	}
	ifs.close();

	//char buf[32];
	//for( int i = 0; i < T; i++ ){
	//	sprintf(buf,"%.7f", t[i] );
	//	ofs << "Case #" << i+1 << ": " << buf << endl;
	//}
	ofs.close();
	system( "pause" );
	return 0;
}
