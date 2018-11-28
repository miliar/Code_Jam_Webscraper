#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <sstream>
#include <ctype.h>  // isdigit(), isalnum(), isalpha()
#include <vector>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <set> // s.insert(elem) -- s.find(elem) != s.end()
#include <math.h>
using namespace std;

// read functions 
// ri(): read int
// rf(): read float
// rd(): read double

#define READF(thetype,format,thename)  thetype thename()  { thetype x; scanf(format,&x); return x;}

READF(int,"%d",ri)
READF(double,"%lf",rd)
READF(float,"%f",rf)

#define MAX_LINE 10000
#define ARRSIZE 1000

bool dbg = false;

#define DBG if( dbg )

#define FOR(var,f,t) for(var=(f); var!=(t); ++var)
#define REP(i,n) FOR(i,0,n)

#define fi(limit) REP(i,limit)
#define fj(limit) REP(j,limit)
#define fk(limit) REP(k,limit)

#define FORSTL(it,n)  for(typeof(x.begin()) it = x.begin(); it != x.end(); it++ )
#define all(v)   v.begin(), v.end()

#define pb push_back

#define CLEAR(arr,value)  memset(arr,value,sizeof(arr))
#define ARR(T,a,n)   T a[n]; CLEAR(a,0);


template <typename T> string a2s( T start, T stop, bool quote=false ) {
    ostringstream os;
    os << "{";
    string comma = "";
    for (T iter = start; iter != stop; ++iter) {
        os << comma << ' ' ;
        if(quote) { os << '\"' << *iter << "\""; }
        else      { os << *iter; }
        // os << ',';
        comma = ",";
    }
    os << " }";
    return os.str();
}

void reopen_io( bool redir = true )
{
    if( redir ) {
        freopen( "input.txt", "r", stdin );
        // freopen( "output.txt", "w", stdout );
    }
}

int reversenr( int n )
{
    int nr = 0;
    while( n > 0 )
    {
        nr = nr*10 + n%10;
        n /= 10;
    }

    return nr;
}

bool isPal( int nr )
{
    if( nr < 0 ) return false;
    if( nr < 10 ) return true;

    return nr == reversenr(nr);
}

int gcnt[1001];

int prepare()
{
    int cnt = 0;
    int lastidx = 0;

    for (int i = 1; i <= 1000; ++i) 
    {
        if( isPal(i) ) {
            int sq = i*i;
            if( sq > 1000) { 
                for (int j = lastidx; j <= 1000; ++j)
                {
                    gcnt[j] = cnt;
                }
                break;
            }
            if( isPal(sq) ) {
                ++cnt;
                gcnt[sq] = cnt; 
                DBG cout << " g[" << sq << "] = " << cnt ;
                DBG cout <<  "  ... completing from " << lastidx+1 << " to " << sq-1 << endl;

                // completar el contador anterior en la tabla gcnt
                for (int j = lastidx+1; j < sq; ++j ) {
                    gcnt[j] = cnt-1;

                }
                lastidx = sq;
            }
        }
    }
    
    int i,j;
    // fi(100) { cout << a2s( gcnt+i*10, gcnt+i*10+10) << endl; }
}

int howmany( int A, int B )
{
    /*
    if( A < 1 ) A = 1;
    if( B > 1000 ) B = 1000;
    if( A > B ) swap( A, B );

    return gcnt[B] - gcnt[A-1];
    */
    // metodo original, ya no lo uso

    int from = int( sqrt(A) - 1);
    int to = int( sqrt(B) + 1 );

    DBG cout << "A = " << A << " B = " << B << endl;

    int cnt = 0;

    for (int i = from; i <= to; ++i)
    {
        if( isPal(i) ) {
            DBG cout << i << " es palindrome " ;
            int sq = i*i;
            DBG cout << sq << " cuadrado " ;
            if( sq > B ) {
                break;
            }
            if( sq >= A && isPal(sq) ) {
                DBG cout << "      tb es palindrome!";
                ++cnt;
            }
            DBG cout << endl;
        }            
    }
    
    return cnt;
}

void testtable()
{
    for ( int i = 1; i <= 1000; ++i)
    {
        for (int j = i; j <= 1000; ++j)
        {
            int hm2 = gcnt[j] - gcnt[i-1];
            if( howmany( i, j ) != hm2 )
            {
                cout << "Problem in combination " << i << " " << j << endl;

            }
        }
    }
}

void doAll()
{
    int i, j, k, n;
    int A, B;
    
    A = ri();
    B = ri();

    if( A < 1 ) A = 1;
    if( B > 1000 ) B = 1000;

    int cnt = howmany( A, B );
    cout << cnt << endl;
}

int main( int argc, char* argv[] ) {

    reopen_io();

    if ( argc != 1 ) dbg = true;

    int i;
    string line;

    prepare(); // testtable();

    int ncases = ri();

    DBG cout << "ncases = " << ncases << "\n";
    REP(i,ncases) {
        cout << "Case #" << (i+1) << ": ";
        doAll();
    }

    return 0;
}

