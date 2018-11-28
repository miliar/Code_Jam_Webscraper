#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

bool is_palindrome( unsigned long long num )
{
	char strchar[20];
	sprintf( strchar, "%llu", num );
	string str = strchar;
	string str_rev = str;
	std::reverse( str_rev.begin(), str_rev.end() );
	return str == str_rev;
}
int main()
{
	int T = 1;
	cin >> T;

	for( int test = 1; test <= T; test++ )
	{
		unsigned int A, B;
		cin >> A >> B;

		A = ceil( sqrt( (double) A ) );
		B = sqrt( (double) B );

		int palCount = 0;
		for( unsigned int i=A; i<=B; i++ )
		{
			if( is_palindrome( i ) && is_palindrome( i*i ) )
			{
				palCount++;
			}
		}
		cout << "Case #" << test << ": " << palCount;
		cout << endl;
	}

	return 0;
}