#include "stdafx.h"

#include <math.h> 
#include <algorithm> 
#include <string> 
#include <vector> 
#include <map> 
#include <set> 
#include <sstream> 
#include <iostream> 
#include <ctype.h> 
#include <list>
#include <queue>
#include <numeric>
#include <fstream>

using namespace std; 

#define VS vector<string> 
#define VI vector<int> 
#define VD vector<double>

#define F(v,s,e) for( int v = (int)(s); v < (int)(e); ++v ) 
#define SET00(x) memset( (x), 0, sizeof(x));
#define SETFF(x) memset( (x), 0xff, sizeof(x));

#define ISS istringstream 
#define OSS ostringstream 

#define i64 long long
#define VI64 vector<i64>

const double PI = 4*atan(1.); 
const double EPS = 1.E-12;


int main(int argc, char* argv[])
{
	ifstream ins("in.txt");
    ofstream outs("out.txt");

    int T; ins >> T;
    F(t,0,T) {
        string S; ins >> S;
		int n = S.length(), lastm = -1;
		int i = n-1, ret = 0;
		while( 1 ) {
			for( ; i >= 0; --i ) {
				if( S[i] == '-' )
					break;
			}
			if( i < 0 ) {
				outs << "Case #" << t+1 << ": " << ret << endl;
				break;
			}
			// top->i must be flipped, but first as much as poss. from top must become '-'
			int ff=0;
			if( S[0] == '+' ) {
				++ret;
				while( S[ff] == '+' ) {
					S[ff++] = '-';
				}
			}

			// check again for finished
			for( i=n-1; i >= 0; --i ) {
				if( S[i] == '-' )
					break;
			}
			if( i < 0 ) {
				outs << "Case #" << t+1 << ": " << ret << endl;
				break;
			}

			//reverse( s.begin(), s.begin()+i+1 );
			
			F(j,0,i/2+1) {
				S[j] = S[j] == '+' ? '-' : '+';
				if( i-j > j )
					S[i-j] = S[i-j] == '+' ? '-' : '+';
				swap( S[j], S[i-j] );
			}
			++ret;
		}
	}	// next testcase
    return 0;
}


