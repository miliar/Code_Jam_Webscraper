#include <iostream>

using namespace std;

int main( int argc, char **argv )
{

  int T;
  cin >> T;
  for ( int i = 0 ; i < T ; ++i )
	{
	  int ans = 0;
	  int sum = 0;
	  int S;
	  cin >> S;
	  string audience;
	  cin >> audience;
	  int len = audience.length();
	  for ( int j = 0 ; j < len ; ++j )
		{
		  sum += ( audience[j] - '0' );
		  if ( sum < j + 1 && ans < j + 1 - sum )
			{
			  ans = j + 1 - sum;
			}
		}
	  cout << "Case #" << i + 1 << ": " << ans << endl;
	}
}
