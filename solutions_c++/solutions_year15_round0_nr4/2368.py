#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
#define DBG(x) cout << ">>> " << #x << " : " << x << endl
#define PB push_back
#define REP(i,b) for ( int i = 0; i < (b); ++i )
#define FOR(i,a,b) for ( int i = (a); i <= (b); ++i )
#define FORD(i,a,b) for ( int i = (a); i >= (b); --i )
#define RI(a) scanf( "%d", &a )
#define RII(a,b) scanf( "%d%d", &a, &b )
#define RIII(a,b,c) scanf( "%d%d%d", &a, &b, &c )
#define RIIII(a,b,c,d) scanf( "%d%d%d%d", &a, &b, &c, &d )
#define DRI(a) int a; RI(a)
#define DRII(a,b) int a, b; RII(a,b)
#define DRIII(a,b,c) int a, b, c; RIII(a,b,c)
#define DRIIII(a,b,c,d) int a, b, c, d; RIIII(a,b,c,d)
const int INF = 1e9+7;

typedef vector<string> shape;

set<shape> shapes[5];
int neigh[4][2] = {
  { +1, +0 },
  { -1, +0 },
  { +0, +1 },
  { +0, -1 }
};

shape rotate( shape sh ) {
  shape s = sh;
  REP( r, 4 )
    REP( c, 4 )
      s[c][3-r] = sh[r][c];
  return s;
}
int x, r, c;
shape canvas, finish;

void print( const shape & s ) {
  REP( r, s.size( ) ) {
    REP( c, s[0].size( ) )
      printf("%c", s[r][c]);
    puts("");
  }
  puts("");
}


void generate( ) {
  shape s( {
    "0000",
    "0000",
    "0000",
    "0000"
  } );
  REP( r, 4 )
    REP( c, 4 ) {
      s[r][c] = '1';
      shapes[1].insert( s );
      s[r][c] = '0';
    }
  FOR( i, 2, 4 ) {
    for ( auto sh : shapes[i-1] ) {
      REP( r, 4 ) {
        REP( c, 4 ) {
          if ( sh[r][c] == '1' ) {
            for ( auto n : neigh ) {
              int r2 = r + n[0], c2 = c + n[1];
              if ( r2 >= 0 && r2 < 4 && c2 >= 0 && c2 < 4 && sh[r2][c2] == '0' ) {
                sh[r2][c2] = '1';
                shapes[i].insert( sh );
                sh[r2][c2] = '0';
              }
            }
          }
        }
      }
    }
  }
  // for ( auto s : shapes[3] ) {
  //   print( s );
  //   REP( r, 4 ) {
  //     REP( c, 4 )
  //       printf("%c", s[r][c]);
  //     puts("");
  //   }
  //   printf("\n");
  // }
}

bool place( const shape & s ) {
  REP( r, s.size( ) )
    REP( c, s[0].size( ) )
      if ( s[r][c] == '1' && ( r >= canvas.size( ) || c >= canvas[0].size( ) || canvas[r][c] == '1'  ) )
        return false;
  REP( r, canvas.size( ) )
    REP( c, canvas[0].size( ) )
      if ( s[r][c] == '1' )
        canvas[r][c] = '1';
  return true;
}

void remove( const shape & s ) {
  REP( r, canvas.size( ) )
    REP( c, canvas[0].size( ) )
      if ( s[r][c] == '1' )
        canvas[r][c] = '0';
}

bool solve( int depth = 1 ) {
  // DBG( depth );
  if ( canvas == finish )
    return true;
  for ( const auto & orig : shapes[x] ) {
    if ( place( orig ) ) {
      if ( solve( depth + 1 ) )
        return true;
      else
        remove( orig );
    }
  }
  return false;
}

bool shift( int dr, int dc, shape & s ) {
  shape sh = shape( s.size( ), string( s[0].size( ), '0' ) );
  REP( r, 4 ) {
    REP( c, 4 ) {
      if ( s[r][c] == '1' ) {
        if ( r + dr < 0 || r + dr >= 4 || c + dc < 0 || c + dc >= 4 )
          return false;
        sh[r+dr][c+dc] = '1';
      }
    }
  }
  s = sh;
  return true;
}

shape flip( bool h, shape s ) {
  if ( h ) {
    REP( r, 4 )
      REP( c, 2 )
        swap( s[r][c], s[r][3-c] );
  } else {
    REP( c, 4 )
      REP( r, 2 )
        swap( s[r][c], s[3-r][c] );
  }
  return s;
}

bool test( set<shape> possible, const shape & s ) {
  shape sh = s;
  REP( i, 4 ) {
    sh = rotate( sh );
    FOR( r, -3, +3 ) {
      FOR( c, -3, +3 ) {
        if ( shift( r, c, sh ) ) {
          if ( possible.find( sh ) != possible.end( ) )
            return true;
        }
      }
    }
  }
  return false;
}

int main( ) {
  generate( );
  DRI( caseCnt );
  FOR( caseNr, 1, caseCnt ) {
    RIII( x, r, c );
    set<shape> impossible, possible;
    printf("Case #%d: ", caseNr );
    
    finish = shape( r, string( c, '1' ) );
    for ( const auto & orig : shapes[x] ) {
      canvas = shape( r, string( c, '0' ) );
      if ( place( orig ) && solve( ) ) {
        possible.insert( orig );
      }
      else {
        impossible.insert( orig );
      }
    }
    // for ( auto s : possible ) 
    //   print( s );
    // DBG( "shit" );
    if ( all_of( impossible.begin( ), impossible.end( ), [&possible] ( const shape & s ) {
      // print( s );
      // print( rotate( s ) );
      // print( rotate( rotate( s ) ) );
      // print( rotate( rotate( rotate( s ) ) ) );


      return ( test( possible, s ) || test( possible, flip( 1, s ) ) ||
        test( possible, flip( 0, s ) ) || test( possible, flip( 0, flip( 1, s ) ) ) );
    } ) ) {
      printf("GABRIEL\n");
    }
    else {
      printf("RICHARD\n");
    }
    for ( const auto & orig : impossible ) {
    }
    next:;
  }


  return 0;
}