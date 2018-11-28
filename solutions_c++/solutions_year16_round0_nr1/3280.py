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

void add_digits( long long num, set<int> &digits ) {
	while( num ) {
		digits.insert( num % 10 );
		num /= 10;
	}
}

int main(int argc, char* argv[])
{
	ifstream ins("in.txt");
    ofstream outs("out.txt");

    int T; ins >> T;
    F(i,0,T) {
        int N; ins >> N;
		if( N == 0 ) {
			outs << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
			continue;
		}
        long long num = N;
		set<int> digits;
		while( num < 2000000000ll*2000000000ll ) {
			add_digits( num, digits );
			if( digits.size() == 10 ) {
				outs << "Case #" << i+1 << ": " << num << endl;
				break;
			}
			num += N;
		}
		
    }
    return 0;
}


/*int main(int argc, char* argv[])
{
	ifstream ins("in.txt");
    ofstream outs("out.txt");

    int T; ins >> T;
    F(i,0,T) {
        int N, K; ins >> N >> K;
        char b[50][50], bc[50][50];
        F(y,0,N) F(x,0,N) {
            ins >> b[y][x];
        }

        F(y,0,N) F(x,0,N) { // rotate board cw
            bc[y][x] = b[N-1-x][y];
        }
        swap( bc, b );

        F(x,0,N) {  // gravity
            F(k,0,N) {
                int dist = 0;
                for( int yy = N-1; yy >= 0; yy-- ) if( b[yy][x] == '.' ) {
                    dist = 1;
                    for( int y = yy; y >= 0; y-- ) {
                        b[y][x] = y > dist ? b[y-dist][x] : '.'; 
                    }
                }
            }
        }

        F(y,0,N) {
            F(x,0,N) { // output board
                outs << b[y][x];
            }
            outs << endl;
        }
        outs << endl;
        //outs << "Case #" << i+1 << ": " << res << endl;
        
    }
    return 0;
}*/

// all your base
/*  int T; ins >> T;
    F(i,0,T) {
        string s; ins >> s;
        int n = s.size();
        map<char,int> sym;
        int digit = 0;
        F(i,0,n) {
            if( sym.find( s[i] ) == sym.end() ) {   // symbol not already in table
                if( digit < 2 )
                    sym[s[i]] = 1 - digit;
                else
                    sym[s[i]] = digit;
                ++digit;
            }
        }
        int base = sym.size();
        if( base == 1 )
            base = 2;
        long long res = 0;
        long long power[64];
        F(j,0,n) {
            power[j] = j ? base*power[j-1] : 1;
            res += sym[s[n-1-j]] * power[j];
        }
        outs << "Case #" << i+1 << ": " << res << endl;
    }*/
    


// center of mass
/*  int T; ins >> T;
    F(i,0,T) {
        int N; ins >> N;
        double x=0,y=0,z=0,vx=0,vy=0,vz=0;
        F(j,0,N) {
            int xx,yy,zz,vxx,vyy,vzz;
            ins >> xx >> yy >> zz >> vxx >> vyy >> vzz;
            x += xx; y += yy; z += zz; vx += vxx; vy += vyy; vz += vzz;
        }
        double v2 = vx*vx + vy*vy + vz*vz;
        if( vx == 0 && vy == 0 && vz == 0 ) {
            double dmin = sqrt( x*x + y*y +z*z ) / N;
            outs << "Case #" << i+1 << ": " << dmin << " " << 0 << endl;
        }
        else {
            double vr = vx*x + vy*y + vz*z;
            double tmin = -vr / v2;
            if( tmin < 0. ) 
                tmin = 0.;
            double xt = x + tmin * vx, yt = y + tmin * vy, zt = z + tmin * vz;
            double dmin = sqrt( xt*xt + yt*yt + zt*zt ) / N;
            outs << "Case #" << i+1 << ": " << dmin << " " << tmin << endl;
        }
    }*/



// prisoners bribe INEFFICIENT
/*int P,Q;

int solve( int *order ) {
    int bribe = 0;
    F(i,0,Q) {  // release all candidates in given order
        int left_limit = 0, right_limit = P;
        F(j,0,i) {  // determine current neighbour interval
            if( order[j] < order[i] && order[j] + 1 > left_limit )
                left_limit = order[j] + 1;
            if( order[j] > order[i] && order[j] < right_limit )
                right_limit = order[j];
        }
        int nn = 0;
        F(j,0,i) {    // determine the number of already released prisoners in neighbourhood ( excluding current limiters )
            if( order[j] > left_limit && order[j] < right_limit-1 )
                ++nn;
        }
        bribe += (right_limit - left_limit - 1 - nn); // bribe all neigbours except current and prior release candidates
    }
    return bribe;
}*/
/*    int T; ins >> T;
    F(i,0,T) {
        ins >> P >> Q;
        int rc[100], res = (1<<31)-1;
        F(j,0,Q) {
            ins >> rc[j];
            --rc[j];
        }
        do {

            res = min( res, solve( rc ) );

        } while( next_permutation( rc, rc+Q ) );

        outs << "Case #" << i+1 << ": " << res << endl;
    }*/


// prisoners good ( DP )
/*int P, Q, rc[100];
int dp[10000][10000];

int solve( int s, int e ) {
if( dp[s][e] > -1 )
    return dp[s][e];
if( e-s <= 1 )
    return dp[s][e] = 0;
int best = 1<<30;
F(i,0,Q) if( rc[i] >=s && rc[i] < e ) {
    best = min( best, e-s-1 + solve(s, rc[i] ) + solve( rc[i]+1, e ) );
}
if( best == 1<<30 )
    best = 0;
return dp[s][e] = best;
}

int main(int argc, char* argv[])
{
	ifstream ins("in.txt");
    ofstream outs("out.txt");

    int T; ins >> T;
    F(i,0,T) {
        ins >> P >> Q;
        F(j,0,Q) {
            ins >> rc[j];
            --rc[j];
        }

        memset( dp, -1, sizeof(dp) );
        int res = solve( 0, P );

        outs << "Case #" << i+1 << ": " << res << endl;
    }
    return 0;
}*/
