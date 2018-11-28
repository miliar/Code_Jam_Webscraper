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
	const int rc = 4;
	ifstream ifs( "A-small-attempt0.in" );
	ofstream ofs( "out" );
	int T;
	ifs >> T;
	for( int i = 0; i < T; i++ ){
		int r1, r2;
		int c1[rc][rc], c2[rc][rc];
		ifs >> r1;
		r1--;
		for( int j = 0; j < rc; j++ ){
			for( int k = 0; k < rc; k++ ){
				ifs >> c1[j][k];
			}
		}
		ifs >> r2;
		r2--;
		for( int j = 0; j < rc; j++ ){
			for( int k = 0; k < rc; k++ ){
				ifs >> c2[j][k];
			}
		}
		int s = 0;
		for( int j = 0; j < rc; j++ ){
			s |= 1<<c1[r1][j];
		}
		int cnt = 0;
		int card = 0;
		for( int j = 0; j < rc; j++ ){
			if( ( 1<<c2[r2][j] & s ) != 0 ){
				card = c2[r2][j];
				cnt++;
			}
		}
		ofs << "Case #" << i+1 << ": ";
		switch( cnt ){
			case 0:
				ofs << "Volunteer cheated!" << endl;
				break;
			case 1:
				ofs << card << endl;
				break;
			default:
				ofs << "Bad magician!" << endl;
		}
	}
	ofs.close();
	ifs.close();
	system( "pause" );
	return 0;
}
