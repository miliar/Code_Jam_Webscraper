#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>

using namespace std;

long long gcd(long long a, long long b)
{
	if ( b == 0 )
	return a;
	else return gcd(b, a % b);
}

int main()
{
	int T ;
	cin >> T;

	for ( int test = 1 ; test <= T ; test++ )
	{
		long long a,b,d;
		char c;
		cin >> a >> c >> b;

		d = gcd(a, b);
		a /= d;
		b /= d;

		long long temp = b;
		while ( temp % 2 == 0 )
		{
			temp /= 2;
		}

		if ( temp != 1 ) 
		{
			cout << "Case #" << test << ": " << "impossible" << endl;
		}
		else {
			int solve = 0;
			while ( a < b )
			{
				b /= 2;
				solve += 1;
			}
			if ( solve <= 40 )
			{
				cout << "Case #" << test << ": " << solve << endl;
			}
			else {
				cout << "Case #" << test << ": " << "impossible" << endl;
			}

		}
	}
}
