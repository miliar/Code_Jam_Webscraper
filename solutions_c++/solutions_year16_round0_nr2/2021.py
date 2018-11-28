#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <deque>

using namespace std;

long T = 0;
long N = 0;
long J = 0;


void flip( string& s, size_t pos )
{
	//cerr << "flip " << pos << endl;
	auto aEnd = s.begin() + pos + 1;
	reverse( s.begin(), aEnd);
	for( auto it = s.begin(); it != aEnd; ++it )
	{
		*it = (*it == '+' ? '-' : '+');
	}
}


size_t Solve( string& s, size_t n )
{
	//cerr << "Solve " << s << ' ' << n << endl; 
	//s ends with - by construction
	auto first = s.find( '-' ); // find the first -
	if( first == 0 )
	{
		flip( s, n - 1 );
		//cerr << s << endl;
		// find last -
		auto it = find( s.rbegin(), s.rend(), '-');
		if( it == s.rend() )
			return 1;

		return 1 + Solve( s, s.size() - (it - s.rbegin()) );
	}
	else
	{
		flip( s, first - 1 );
		//cerr << s << endl;
		return 1 + Solve( s, n );
	}
}


int main(int argc, char * argv[] )
{
	
	cin >> T;

	for( auto t=0; t<T; ++t )
	{
		cout << "Case #" << t+1 << ": " ;
		string s;
		cin >> s;
		//cerr << s << endl;
		auto it = find( s.rbegin(), s.rend(), '-');
		if( it == s.rend() )
			cout << '0' << endl;
		else
			cout << Solve( s, s.size() - (it - s.rbegin()) ) << endl;

	}
	return 0;
}
