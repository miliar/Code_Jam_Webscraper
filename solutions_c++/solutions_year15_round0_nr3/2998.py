
//--------------------------------------------------------------------------
// Require-header-file(s)
//--------------------------------------------------------------------------

// Standard-library
#include <algorithm>
#include <deque>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>

// Common using type
typedef bool                    bool_type;
typedef size_t                  size_type;
typedef long long               item_type;
typedef std::deque< item_type > ideq_type;

enum { NK=-4, NJ=-3, NI=-2, N1=-1, V0=0, P1=1, PI=2, PJ=3, PK=4 };

// -  1  I  J  K
// 1  1  I  J  K 
// I  I -1  K -J
// J  J -K -1  I
// K  K  J -I -1
long cross( long v1,
            long v2 )
{
  static long const value[5][5] =
  {
    V0, P1, PI, PJ, PK,
    P1, P1, PI, PJ, PK,
    PI, PI, N1, PK, NJ,
    PJ, PJ, NK, N1, PI,
    PK, PK, PJ, NI, N1
  };

  long r = std::abs( v1 );
  long c = std::abs( v2 );
  long v = value[r][c];

  if( v1 < 0 ) v *= -1;
  if( v2 < 0 ) v *= -1;

  return v;
}

int evaluate( char c )
{
       if( c == 'i' ) return PI;
  else if( c == 'j' ) return PJ;
  else if( c == 'k' ) return PK;

  return V0;
}

long evaluate( std::string s,
               size_t      f =  0,
               size_t      t = -1 )
{
  long r = 1;

  size_t N = s.size( );
  if( t > N ) t = N;

  for( size_t i = f; i < t; ++i )
    r = cross( r, evaluate( s[i] ) );

  return r;
}

long repeat_evaluate( long   s,
                      size_t r )
{
  if( r == 0 ) return 1;
  if( r == 1 ) return s;

  int v = 0;
  {
    int t = repeat_evaluate( s, r/2 );
    v = cross( t, t );
  }

  if( r & 1 ) v = cross( v, s );
  
  return v;
}

struct evaluate_result
{
  size_t round;
  size_t index;
};

bool evaluate_to( std::string       s,
                  long              v,
                  long              t,
                  size_t            m,
                  evaluate_result & e )
{
  if( m == 0 ) return false;
  if( v == t ) return true;

  // Continue from previous
  size_t N = s.size( );
  for( size_t i = e.index; i < N; ++i )
  {
    v = cross( v, evaluate( s[i] ) );
    if( v == t )
    {
      e.index = (i + 1) % s.size( );
      return true;
    }
  }

  // Go on
  evaluate_result e2{ 0,0 };
  for( --m; m > 0; --m )
  {
    for( size_t i = 0; i < N; ++i )
    {
      v = cross( v, evaluate( s[i] ) );
      if( v == t )
      {
        e.round += e2.round;
        e.index = (i + 1) % N;
        return true;
      }
    }

    e2.round += 1;
  }

  return false;
}

int main( int     argc, 
          char ** argv )
{
  char result[][8] =
  {
    "NO",
    "YES"
  };

  size_t T; 
  std::cin >> T;

  // Foreach test case
  for( size_t t = 1; t <= T; ++t )
  {
    size_t l, r;
    std::string s;
    std::cin >> l >> r >> s;

    bool is_success = false;
    if( l >= 2 )
    {
      if( N1 == repeat_evaluate( evaluate( s ), r ) )
      {
        evaluate_result e{0, 0};

        if( true == evaluate_to( s, P1, PI, r          , e ) )
        if( true == evaluate_to( s, P1, PJ, r - e.round, e ) )
        if( true == evaluate_to( s, P1, PK, r - e.round, e ) )
          is_success = true;
      }
    }

    std::cout
      << "Case #" << t << ": "
      << result[is_success] << std::endl;
  }

  return 0;
}

//--------------------------------------------------------------------------
// End-of-file
//--------------------------------------------------------------------------

