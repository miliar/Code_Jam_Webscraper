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
int compare( const void *pa, const void *pb ){//int[][], qsort
	const int *a = (int*)pa;
	const int *b = (int*)pb;
	return a[0] - b[0];
}
int main(){
	//ifstream ifs( "B-small-attempt1.in" );
	//ifstream ifs( "B-sample.in" );
	ifstream ifs( "B-large.in" );
	int T, N;
	const int Nmax = 1000;
	int A[Nmax][2] = {};
	int B[Nmax] = {};
	ifs >> T;
	ofstream ofs( "out" );
	for( int i = 1; i <= T; i++ ){
		ifs >> N;
		for( int j = 0; j < N; j++ ){
			ifs >> A[j][0];
			A[j][1] = j;//0: val. 1: original pos
			B[j] = j;//[original pos] = updated pos
		}
		qsort( A, N, sizeof(A[0]), compare );
		//algorithm
		//for( int j = 0; j < N; j++ )cout << A[j][0] << " ";
		//cout << endl;
		int cnt = 0, p = 0, q = N-1;
		for( int j = 0; j < N; j++ ){
			int dist1 = B[A[j][1]]-p;
			int dist2 = q - B[A[j][1]];
			if( dist1 > dist2 ){
				cnt += dist2;
				q--;
				for( int k = A[j][1]; k < N; k++ ){
					B[k]--;
				}
			}else{
				cnt += dist1;
				p++;
				for( int k = A[j][1]; k >=0; k-- ){
					B[k]++;
				}
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
	//system( "pause" );
	return 0;
}
