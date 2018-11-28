#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

#define MAXL 10005

using namespace std;

int t, n, X, L, sum;
char text[MAXL+1];

map < pair<string,string>, string> m;
int sI[MAXL], sK[MAXL];
int cntsI, cntsK;

string word;

string idx[] = { "1", "i", "j", "k" };
string p[4][4] = {
    { "1", "i", "j", "k" },
    { "i", "-1", "k", "-j" },
    { "j", "-k", "-1", "i" },
    { "k", "j", "-i", "-1" }
};

string next( string s1, string s2 ) {

    bool f = false;

    string ret;
    
    string w1, w2;
    
    if ( s1.size() == 2 ) {
        w1 = s1[1];
        f = !f;
    }else {
        w1 = s1[0];
    }
    
    if ( s2.size() == 2 ) {
        w2 = s2[1];
        f != f;
    }else {
        w2 = s2[0];
    }
    
    ret += m[ make_pair( w1, w2 ) ];
   
    if ( f ) {
        if ( ret.size() == 2 ) {
            ret.erase( ret.begin() );
        }else {
            ret.insert( ret.begin(), '-' );
        }
    }
   
    return ( ret );

}

struct state {
    string val;
};

state node[4*MAXL];

state combine( state q1, state q2 ) {

    state ret;
    
    ret.val = next( q1.val, q2.val );
    
    return ( ret );

}

void build( int v, int x, int y ) {

    if ( x == y ) {
        int idx = max( 1, x % (L+1) ) - 1;
        node[v].val = text[ idx ];
        return;
    }
    
    int mid = ( x + y ) / 2;
    
    build( 2*v, x, mid );
    build( 2*v+1, mid+1, y );
    
    node[v] = combine( node[2*v], node[2*v+1] );

}

state query( int v, int x, int y, int qx, int qy ) {

    if ( qx == x && qy == y ) {
        return ( node[v] );
    }
    
    int mid = ( x + y ) / 2;
    
    if ( qy <= mid ) {
        return ( query( 2*v, x, mid, qx, qy ) );
    }else if ( qx > mid ) {
        return ( query( 2*v+1, mid+1, y, qx, qy ) );
    }else {
        state q1, q2;
        q1 = query( 2*v, x, mid, qx, mid );
        q2 = query( 2*v+1, mid+1, y, mid+1, qy );            
        return ( combine( q1, q2 ) );
    }
    
}

bool has_i( int f ) {
    return ( f & (1<<0) );
}

bool has_j( int f ) {
    return ( f & (1<<1) );
}

bool has_k( int f ) {
    return ( f & (1<<2) );
}

inline void readi(int &v){
    char c;
    while( (c=getchar())<'0' || c > '9' );
    v = c-'0';
    while( (c=getchar())>='0' && c <= '9' ) v = v*10 + c-'0';
}

int main( ) {

    for ( int i = 0; i < 4; ++i )
        for ( int j = 0; j < 4; ++j )
            m.insert( make_pair( make_pair( idx[i], idx[j] ), p[i][j] ) );
            
    //cout << next( next( "j", "i" ), "j" ) << endl;
   
    readi( t );//scanf( "%d", &t );
    
    for ( int T = 0; T < t; ++T ) {
        
        readi( L );
        readi( X );
        scanf( "%s", text );
        
        int n = L*X;
        
        int idx = 0;
        
        //cout << text << endl;
        
        string cur;
        cur += text[0];
        
        int f = 0;
        bool found_su = false;
        
        if ( cur[0] == 'i' ) {
            f |= 1;
            found_su = true;
        }
        
        for ( int i = 1; i < L*X; ++i ) {
        
            if ( found_su ) {
                cur = "";
                cur += text[ (i%L) ];
            }else {
                string w = "";
                w += text[ (i%L) ];
                cur = next( cur, w );
            }
            
            found_su = false;
            
            if ( cur[0] == 'i' && !has_i( f ) ) {
                f |= (1<<0);
                found_su = true;
                //printf( " (FOUND i) " );
            }else if ( cur[0] == 'j' && !has_j( f ) && has_i( f ) ) {
                f |= (1<<1);
                found_su = true;
                //printf( " (FOUND j) " );
            }
        
        }
        
        bool found = false;
        
        if ( cur[0] == 'k' && has_i(f) && has_j(f) ) {
            found = true;
        }
        
        if ( found ) {
            printf( "Case #%d: YES\n", T+1 );
        }else {
            printf( "Case #%d: NO\n", T+1 );
        }
       
    }

    return 0;

}