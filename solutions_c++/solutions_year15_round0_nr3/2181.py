#include <iostream>
#include <vector>

using namespace std;

const int i = 2;
const int j = 3;
const int k = 4;

int map[ 5 ][ 5 ] =
  {{ 0, 0, 0, 0, 0 },
   { 0, 1, i, j, k },
   { 0, i, -1, k, -j },
   { 0, j, -k, -1, i },
   { 0, k, j, -i, -1 }};   

int invmap[ 5 ][ 5 ] =
  {{ 0, 0, 0, 0, 0 },
   { 0, 1, i, j, k },
   { 0, -i, 1, -k, j },
   { 0, -j, k, 1, -i },
   { 0, -k, -j, i, 1 }};

struct mystring {
  vector<int> input;
  int X;
  int L;

  mystring( string input, int X ) {
	for ( int i = 0; i < input.length(); i++ )
	{
	  this->input.push_back( input[ i ] - 'i' + 2 );
	}
	this->X = X;
	L = input.length();
  }

  int operator[]( int v ) {
	return input[ v % L ];
  }

  size_t length() {
	return X * L;
  }  
};

// n * ret = m
int inv( int n, int m )
{
  int sign = ( n * m ) / abs( n * m );
  int na = abs( n );
  int ma = abs( m );
  return sign * invmap[ na ][ ma ];
}

int times( int n, int m )
{
  int sign = ( n * m ) / abs( n * m );
  int na = abs( n );
  int ma = abs( m );
  return sign * map[ na ][ ma ];
}

int times( mystring &vs, int s, int e )
{
  int ans = vs[ s ];
  for ( int a = s + 1; a < e; a++ )
  {
	ans = times( ans, vs[ a ] );
  }
  return ans;
}

bool solve( mystring &vs )
{
  int L = vs.length();
  if ( L < 3 ) return false;

  int n3_state = times( vs, 0, L );
  int n1 = 1;
  
  for ( int a = 1; a < L - 1; a++ ) {
	n3_state = inv( vs[ a - 1 ], n3_state );
	n1 = times( n1, vs[ a - 1 ] );
	int n2 = 1;
	int n3 = n3_state;
	for ( int b = a + 1; b < L; b++ ) {
	  n2 = times( n2, vs[ b - 1 ] );
	  n3 = inv( vs[ b - 1 ], n3 );
	  if ( n1 == i && n2 == j && n3 == k ) {
		return true;
	  }
	}
  }
  return false;
}

int main()
{
  int T;
  cin >> T;
  for ( int t = 1; t <= T; t++ )
  {
	int L, X;
	cin >> L >> X;
	string str;
	cin >> str;
	mystring input( str, X );

	if ( solve( input ) ){
	  printf( "Case #%d: YES\n", t );
	} else {
	  printf( "Case #%d: NO\n", t );
	}
  }
}
