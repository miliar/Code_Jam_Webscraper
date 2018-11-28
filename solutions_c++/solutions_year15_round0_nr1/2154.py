#include <iostream>

using namespace std;

int main()
{
  int t;
  cin >> t;
  for ( int i = 1; i <= t; i++ )
  {
	int smax;
	string d;
	cin >> smax >> d;
	int accum = 0;
	int ans = 0;
	for ( int j = 0; j <= smax; j++ )
	{
	  int v = d[ j ] - '0';
	  if ( accum < j )
	  {
		ans += j - accum;
		accum = j;
	  }
	  accum += v;
	}
	printf( "Case #%d: %d\n", i, ans );
  }
}
