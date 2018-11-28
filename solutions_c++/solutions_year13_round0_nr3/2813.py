#include <iostream>
using namespace std;
int is_palindrome(int x )
{
	int rev_x = 0, orig_x = x;
	while ( x )
	{
		rev_x = rev_x * 10 + ( x % 10 );
		x = x / 10;
	}
	return orig_x == rev_x;
}
int main ( int argc, char * argv[] )
{
	int n;
	cin >> n;
	for ( int tc = 1 ; tc <= n ; tc++ )
	{
		int a, b, i, inc=1, isqrt = 0, fns = 0;
		cin >> a >> b;
		for ( i = 0, isqrt = 0 ; i < a ; i+= inc, inc += 2, isqrt++ )
                     ;
		for ( ; i <= b ;  i+= inc, inc += 2 , isqrt++ )
			if ( is_palindrome(isqrt) && is_palindrome ( i ) )
				fns++;
		cout << "Case #" << tc << ": " << fns << endl;
	}
}
		

