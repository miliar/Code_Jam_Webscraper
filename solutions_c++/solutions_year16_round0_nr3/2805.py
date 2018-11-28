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

bool pr[100000000];	// to 1e8

void sieve( int n ) { 
	F(j,0,n) pr[j] = true;
	int m = (int)sqrt( (double)n ); 
	pr[0] = pr[1] = false;
	for( int i = 2; i <= m; ++i ) 
		if( pr[i] ) 
			for( int k = i * i; k <= n; k += i ) {
				pr[k] = false; 
			}
} 


int main(int argc, char* argv[])
{
	ifstream ins("in.txt");
    ofstream outs("out.txt");

	sieve( 100000000 );
	outs << "Case #1:" << endl;

	int T,N,J; ins >> T >> N >> J;
	int candidate = (1<<(N-1)) + 1;
	int count = 0;
	while( count < J ) {
		bool good = true;
		long long rep[11] = {0,0,0,0,0,0,0,0,0,0};
		long long fac[11] = {0,0,0,0,0,0,0,0,0,0};
		F(i,2,11) {	// base-i representations
		
			long long base = 1;
			F(j,0,N) {
				rep[i] += base * ( ( candidate & (1<<j) ) ? 1 : 0 );
				base *= i;
			}
			if( rep[i] < 100000000 ) {
				if( pr[rep[i]] ) {	// candidate not suitable as jam coin
					good = false;
					break;
				}
			}
			{ // search for a small prime factor, if none treat rep[i] like a prime

				long long fact = 2;
				while( fact*fact <= rep[i] ) {	// might look for smaller prime factors only
					if( rep[i] % fact == 0 ) {
						fac[i] = fact;
						break;
					}
					++fact;
					while( !pr[fact] ) ++fact;
				}	// try next prime fac
				if( fac[i] == 0 ) {
					good = false;
					break;
				}
			}
		}	// next base
		if( good ) {
			outs << rep[10];
			
			// get prime factors for all rep[i]
			F(i,2,11) {
				outs << ' ' << fac[i];				
				/*long long fac = 2;
				while( fac*fac <= rep[i] ) {
					if( rep[i] % fac == 0 ) {
						outs << ' ' << fac;
						break;
					}
					++fac;
					while( !pr[fac] ) ++fac;
				}	// try next prime fac*/
			}
			
			outs << endl;
			++count;
		}
		candidate += 2;
	}

    
	return 0;
}


