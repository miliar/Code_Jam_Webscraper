//============================================================================
// Name        : FairAndSquareSmall.cpp
// Author      : Anmol Ahuja
//============================================================================

#include <cstdio>
#include <cmath>
#include <iostream>
using namespace std;

template <class T>
bool isPalindrome( T n )
{
	T rev=0, num=n;
	while(n!=0)
	{
		rev*=10;
		rev+=n%10;
		n/=10;
	}
	if(rev==num)
		return true;
	return false;
}

bool hasPalindromeRoot( int n )
{
    int t = (int) floor( sqrt(n) + 0.5 );
    if( t*t == n && isPalindrome(t) )
    	return true;
    return false;
}

int numFairAndSquare( int lower, int upper )
{
	int num=0;
	while( lower<=upper )
	{
		if( isPalindrome(lower) && hasPalindromeRoot(lower) )
			++num;
		++lower;
	}
	return num;
}

int main() {
	int t,x;
	int lower,upper;
	scanf("%d",&t);
	for( x=1; x<=t; ++x)
	{
		scanf("%d %d", &lower, &upper);
		printf( "Case #%d: %d\n", x, numFairAndSquare( lower, upper ) );
	}
	return 0;
}
