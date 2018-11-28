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
#include <stdlib.h>
//#define FOR( i, N ) for( int (i) = 0; (i) < (N); (i)++ )
//#define FOR_( i, start, endplusone ) for( int (i) = (start); (i) < (endplusone); (i)++ )
const double EPS = 1e-10;
const double PI = 3.141592653589793;
using namespace std;
int compare( const void * a, const void * b ){
	if ( *(double*)a <  *(double*)b ) return -1;
	if ( *(double*)a == *(double*)b ) return 0;
	if ( *(double*)a >  *(double*)b ) return 1;
}
int main(){
	ifstream ifs( "D-large.in" );
	ofstream ofs( "out" );
	ofstream view( "view" );
	int T, N;
	ifs >> T;
	double *nao, *ken;
	nao = new double[1000];
	ken = new double[1000];
	for ( int i = 0; i < T; i++ ){
		ifs >> N;
		for ( int j = 0; j < N; j++ ){
			ifs >> nao[j];
		}
		for ( int j = 0; j < N; j++ ){
			ifs >> ken[j];
		}
		qsort( nao, N, sizeof(double), compare);
		qsort( ken, N, sizeof(double), compare);

		for ( int j = 0; j < N; j++ ){
			view << left << setw(6) << nao[j];
		}
		view << endl;
		for ( int j = 0; j < N; j++ ){
			view << left << setw(6) << ken[j];
		}
		view << endl;

		int cnt, naopos, kenpos, kenN = N;
		cnt = naopos = kenpos = 0;
		//for ( int j = 0; j < N; j++ ){
		//	if ( nao[j] > ken[j] ){
		//		cnt++;
		//	}
		//}
		while ( kenpos < kenN && naopos < N ){
			if ( nao[naopos] > ken[kenpos] ){
				cnt++;
				naopos++;
				kenpos++;
			} else {
				naopos++;
				kenN--;
			}
		}

		view << "Case #" << i+1 << ": " << cnt << " ";
		ofs << "Case #" << i+1 << ": " << cnt << " ";



		cnt = naopos = kenpos = 0;
		while ( kenpos < N ){
			if ( nao[naopos] > ken[kenpos] ){
				cnt++;
				kenpos++;
			} else {
				naopos++;
				kenpos++;
			}
		}
		view << cnt << endl << endl;
		ofs << cnt << endl;
	}
	ofs.close();
	view.close();

	//system( "pause" );
	delete[] ken, nao;
	return 0;
}
