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
        int N; ins >> N;
		int P[26]; F(i,0,N) ins >> P[i];
		outs << "Case #" << t+1 << ":";
		int maxp=0, imaxp=-1;
		if( N > 2 ) {
			do {
				maxp=0, imaxp=-1;
				int nmaxp = 0, omaxp = -1; 
				F(i,0,N) {
					if( P[i] > maxp ) {
						maxp = P[i];
						imaxp = i;
						nmaxp = 1;
					}
					else if( P[i] == maxp ) {
						++nmaxp;
						omaxp = i;
					}
				}
				if( maxp == 0 )
					break;
				if( nmaxp == 2 ) {
					outs << ' ' << (char)(imaxp+'A') << (char)(omaxp+'A');
					--P[imaxp]; --P[omaxp];
				}
				else {
					outs << ' ' << (char)(imaxp+'A');
					--P[imaxp];
				}
			} while( 1 );
		}
		else {
			while( P[0] > P[1] ) {
				outs << ' ' << 'A';
				--P[0];
			}
			while( P[1] > P[0] ) {
				outs << ' ' << 'B';
				--P[1];
			}
			while ( P[0] ) {
				outs << ' ' << "AB";
				--P[0];
			}
		}
		
		outs << endl;
	
	}	// next testcase
    return 0;
}


