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
using namespace std;

// read functions 
// ri(): read int
// rf(): read float
// rd(): read double

#define READF(thetype,format,thename)  thetype thename()  { thetype x; scanf(format,&x); return x;}

READF(int,"%d",ri)
READF(double,"%lf",rd)
READF(float,"%f",rf)

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

bool checkok( int a[100][100], int N, int M, int x, int y )
{
    // DBG cout << "Checking " << x << "," << y << endl;
    bool ok = true;

    int val = a[x][y];
    ostringstream errmsg;

    for (int j = 0; j < M; ++j)
    {
        if( a[x][j] > val ) {
            errmsg << " prblm while checking " << val << " in (" << x << "," << y << "), " << a[x][j] << " en (" << x << "," << j <<") > " << val << endl;
            ok = false;
            break;
        }
    }

    if(!ok) {
        ok = true;
        for (int i = 0; i < N; ++i)
        {
            if( a[i][y] > val ) {
                errmsg << " prblm while checking " << val << " in (" << x << "," << y << "), " << a[i][y] << " en (" << i << "," << y <<") > " << val << endl;
                ok = false;
                break;
            }
        }
    }

    DBG if( !ok ) { cout << errmsg.str() << endl; }

    return ok;
}

void doAll()
{
    int a[100][100];
    int i, j;

    int N, M;

    N = ri();
    M = ri();

    fi(N) fj(M) { a[i][j] = ri(); }

    DBG {
        cout << endl;
        fi(N) { cout << a2s(a[i],a[i]+M) << endl; }
        cout << endl;
    }

    bool ok = true;
    fi(N) { 
        if(!ok) break; 
        fj(M) {
            if(!ok) break;
            ok = checkok(a,N,M,i,j);  
        }
    }
    
    cout << (ok?"YES":"NO") << endl;
}

int main( int argc, char* argv[] ) {

    reopen_io();

    if ( argc != 1 ) dbg = true;

    int i;
    string line;

    int ncases = ri();

    DBG cout << "ncases = " << ncases << "\n";
    REP(i,ncases) {
        cout << "Case #" << (i+1) << ": ";
        doAll();
    }

    return 0;
}