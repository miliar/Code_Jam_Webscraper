#include <iostream>
#include <vector>
#include <array>
#include <algorithm>

using namespace std;

long T = 0;
long N = 0;

void updateSeen( array<bool, 10>& seen, long n )
{
	while( n )
	{
		auto d = n%10;
		seen[ d ] = true;
		n /= 10;
	}
}


int main(int argc, char * argv[] )
{
	cin >> T;
	for( auto t=0; t<T; ++t )
	{
		cin >> N;
		cout << "Case #" << t+1 << ": ";

		if( N == 0)
		{
			cout << "INSOMNIA" << endl;
			continue;
		}
		array<bool, 10> seen = {false,false,false,false,false,false,false,false,false,false};
		auto n = 0;
		while( ! all_of( seen.begin(), seen.end(), []( bool isSeen ){return isSeen;} ) )
		{
			n+=N;
			updateSeen( seen, n );
		}

		cout << n << endl;
	}
	return 0;
}