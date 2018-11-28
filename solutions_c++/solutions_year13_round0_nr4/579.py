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

#define CHECKAVAIL

bool dbg = false;

#define DBG if( dbg )

#define FOR(var,f,t) for(var=(f); var!=(t); ++var)
#define REP(i,n) FOR(i,0,n)

#define fi(limit) REP(i,limit)
#define fj(limit) REP(j,limit)
#define fk(limit) REP(k,limit)

#define FORSTL(it,x)  for(typeof(x.begin()) it = x.begin(); it != x.end(); it++ )
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
    // freopen("sample.txt","r",stdin);
    // freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
    // freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
    // freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

    if( redir ) {
        freopen( "input.txt", "r", stdin );
        // freopen( "output.txt", "w", stdout );
    }
}

struct ChestInfo
{
   bool open;
   int lock;
   vector<int> ki;  // keys inside

   void show() {
     cout << "open:" << (open?"Yes":"No ") << " " << " lock:" << lock << " ";
     cout << "   keys inside: { ";
     FORSTL( it, ki ) cout << *it << " ";
     cout << "}";
   }
};

void closeChest( ChestInfo& ch )
{
    ch.open = false;
}

void showChest( ChestInfo& ch )
{
    ch.show();
    cout << endl;
}

string indent(int level)
{
    ostringstream os;
    
    int i;
    fi(level) os << "  ";

    return os.str();
}

void doAll(int caseno)
{
    int i, j, k, n;
    int K, N;
    int mykeys[401];
    CLEAR(mykeys,0);

    K = ri();  // numbers of keys
    N = ri();  // number of chests

    ARR( int, a, K );
    fi(K) { a[i] = ri(); ++mykeys[a[i]]; }

    ARR( ChestInfo, chests, N+1 );

    // cout << a2s(a,a+K) << endl;

    fi(N)
    {
       int Ti = ri();
       int Kn = ri();

       chests[i+1].open = false;
       chests[i+1].lock = Ti;

       fj(Kn) { chests[i+1].ki.push_back( ri() );  }
    }

    DBG {
        cout << endl;
        for( k = 1; k <= N; ++k )
        {
            cout << (k<10?" ":"") << k << " ";
            chests[k].show();
            cout << endl;
        }
        // cout << "Chests" << endl;
        // for_each( chests+1, chests+N+1, showChest );
    }

    ARR(int,need,N+1);
    ARR(int,support,N+1);
    int l = 0;     // level we're at
    int ch2o = 0;  // chest to open
    ARR(int,p,N);
    while( l >= 0 ) {

        if( p[l] != 0 ) {
            FORSTL(it,chests[p[l]].ki) {
                --mykeys[*it];
            }
            // la llave que gaste en abrir el chest la recupero
            ++mykeys[ chests[p[l]].lock ];
            chests[p[l]].open = false;
        }

        #ifdef CHECKAVAIL

        // evaluar si tiene sentido entrar siquiera a este nivel, considerando las necesidades de las 
        // chests cerradas. Si ellas requieren un numero determinado de llaves (por ejemplo, entre todas
        // requieren 3 llaves de tipo 1, 5 llaves de tipo 2, etc) y ver si entre las llaves que ya tengo
        // mas las que consiga abriendolas, menos las que gaste abriendolas a ellas, me da un nro positivo.
        // Si da negativo -> abortar este nivel
        CLEAR(need,0);
        CLEAR(support,0);
        for( i = 1; i <= N; ++i ) {
            if( !chests[i].open ) {
                ++need[chests[i].lock];
                FORSTL( it, chests[i].ki ) {
                    ++support[*it];
                }
            }
        }

        DBG {
            for( i = 1; i <= N; ++i )
            {
                if( need[i] > mykeys[i] ) {
                    cout << " < ";
                }
                else {
                    cout << "   ";
                }
            }
            cout << "}" << endl;
        }

        // Les resto las que ya tengo
        bool possible = true;
        for( i = 1; i <= N; ++i ) {
            if( need[i] > 0 ) {
                need[i] -= mykeys[i];

                if( need[i] > 0 ) {
                    possible = false;
                }
            }
        }


        if( !possible) {
            possible = true;
            for( i = 1; i <= N; ++i ) {
                int thelock = chests[i].lock;

                if( !chests[i].open && need[thelock] > 0 ) {

                    bool found1provider = false;
                    // Alguien mas podria proveer de la llave que necesito?
                    for( j = 1; j <= N; ++j ) {
                        if( i != j ) {
                            // recorrer las llaves que el resto de las chests cerradas tienen
                            if( !chests[j].open ) {
                                FORSTL( it, chests[j].ki ) {
                                    if( *it == thelock ) {
                                        found1provider = true;
                                        break;
                                    }
                                }
                            }

                        }
                    }

                    // o podria ser yo mismo el provider, siempre que las llaves que ahora tengo sean > 0
                    if( mykeys[chests[i].lock] > 0 ) {
                        FORSTL( it, chests[i].ki ) {
                            if( *it == thelock ) {
                                found1provider = true;
                                break;
                            }
                        }
                    }

                    if( !found1provider ) {
                        possible = false;
                        break;
                    }
                }
            }

            if( possible ) {
                // Chequear si el total de los aportes es al menos igual a lo necesitado
                for( i = 1; i <= N; ++i ) {
                     if( need[i]>support[i]) {
                        possible = false;
                        break;
                     }
                 }
            }
        }

        if( !possible )
        {

            --l;
            continue;
        }
        #endif

        DBG {
            for( k = 1; k <=N; ++k ) {
                if( chests[k].open )
                    cout << k << " ";
            }
            cout << "} closed { ";
            for( k = 1; k <= N; ++k ) {
                if( !chests[k].open )
                    cout << k << ":" <<  chests[k].lock << " ";
            }
            cout << "}" << endl;
        }

        ch2o = 0;
        // search chest to epen
        for (int i = p[l]+1; i <= N; ++i)
        {
            // do I have the key to open a closed chest?
            if( !chests[i].open && mykeys[chests[i].lock] > 0 ) {
                ch2o = i;
                break;
            }
        }

        if( ch2o != 0 ) {
            chests[ch2o].open = true;
            p[l] = ch2o;
            --mykeys[chests[ch2o].lock];
            FORSTL(it,chests[ch2o].ki) {
                ++mykeys[*it];
            }
            ++l;
            if( l >= N )
            {
                // print answer, return
                fk(N) { 
                    cout << p[k];
                    if( k != N-1 ) 
                        cout << " "; 
                }
                cout << endl;
                return;
            }
        }
        else
        {
            p[l] = 0;
            --l;
        }

    }
    cout << "IMPOSSIBLE" << endl;

}



int main( int argc, char* argv[] ) {

    reopen_io();

    if ( argc != 1 ) dbg = true;

    int i;
    string line;

    int ncases = ri();

    REP(i,ncases) {
        cout << "Case #" << (i+1) << ": ";
        doAll(i);
    }

    return 0;
}

