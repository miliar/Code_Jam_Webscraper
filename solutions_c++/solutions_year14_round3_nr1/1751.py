#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <iomanip>
#include <cassert>

using namespace std;

unsigned int mylog2( unsigned int val )
{
	unsigned int ret = -1;
	while( val != 0 )
	{
		val >>= 1;
		ret++;
	}
	return ret;
}

bool isPowerOf2( unsigned x )
{
	return !(x == 0) && !(x & (x - 1));
}

int main()
{
	unsigned t;
	cin >> t;

	for( unsigned i = 1; i <= t; ++i )
	{
		string temp;
		cin >> temp;
		auto it = temp.find("/");
		assert(it != temp.size() );
		temp[it] = ' ';
		stringstream ss;
		ss << temp;

		unsigned a, b;
		ss >> a >> b;

		if( isPowerOf2( b ) == false )
		{
			cout << "Case #" << i << ": impossible" << "\n";
			continue;
		}
		
		unsigned x = b / 2;
		unsigned ans = 1;
		while( a < x )
		{
			++ans;
			x /= 2;
		}

		cout << "Case #" << i << ": " << ans << "\n";
	}

	return 0;
}