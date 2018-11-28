
#include <iostream>

#include <vector>
#include <string>

using namespace std;

int tests;

inline bool is_p( long long v )
{
	static int d[32];
	static int idx;

	if ( v < 10 ) return true;

	idx = 0;
	while( v > 0 )
	{
		d[idx++] = v%10;
		v /= 10;
	}
	// check
	const auto kHI =idx/2;
	for( int i=0; i<kHI; ++i )
	{
		if ( d[i] != d[idx-1-i] ) return false;
	}
	return true;
}

int main()
{
	cin >> tests;

	for( int curTest=0; curTest<tests; ++curTest )
	{
		long long a, b;
		cin >> a >> b;

		long long res = 0;
		long long i = 0;
		while( i*i < a )
		{
			++i;
		}
		while( i*i <= b )
		{
			if ( is_p(i) && is_p(i*i) ) ++res;
			++i;
		}

		cout << "Case #" << (curTest+1) << ": ";
		cout << res;
		cout << endl;
	}

	return 0;
}

