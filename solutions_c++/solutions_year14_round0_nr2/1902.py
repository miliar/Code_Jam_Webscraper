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
//#define FOR( i, N ) for( int (i) = 0; (i) < (N); (i)++ )
//#define FOR_( i, start, endplusone ) for( int (i) = (start); (i) < (endplusone); (i)++ )
const double EPS = 1e-10;
const double PI = 3.141592653589793;
using namespace std;

int main(){
	ifstream ifs( "B-large.in" );
	int T;
	ifs >> T;
	double *t = new double[T];
	for( int i = 0; i < T; i++ ){
		double C, F, X, V = 2.0;
		ifs >> C >> F >> X;
		double XmC = X-C;
		double tprev = DBL_MAX, tcurr = X/V;
		int n = 0;
		while( tprev > tcurr ){
			tprev = tcurr;
			tcurr = tprev - XmC/(V+n*F) + X/(V+(n+1)*F);
			n++;
		}
		//cout << n << endl;
		t[i] = tprev;
	}
	ifs.close();
	ofstream ofs( "out" );
	char buf[32];
	for( int i = 0; i < T; i++ ){
		sprintf(buf,"%.7f", t[i] );
		ofs << "Case #" << i+1 << ": " << buf << endl;
	}
	ofs.close();
	system( "pause" );
	return 0;
}
