#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for ( int t = 1; t <= T; t++ )
  {
	int d;
	cin >> d;
	vector<int> vs( d );
	int v_max = 0;
	for ( int i = 0; i < d; i++ )
	{
	  cin >> vs[ i ];
	  v_max = max( v_max, vs[ i ] );
	}
	int min_turn = 10000000;
	for ( int k = 1; k <= v_max; k++ )
	{
	  int turn = 0;
	  for ( int i = 0; i < d; i++ )
	  {
		turn += ( vs[ i ] + k - 1 ) / k - 1;
	  }
	  turn += k;
	  // cerr << k << " " << turn << endl;
	  min_turn = min( min_turn, turn );
	}
	// cerr << "case " << t << endl;
	printf( "Case #%d: %d\n", t, min_turn );
  }
}
