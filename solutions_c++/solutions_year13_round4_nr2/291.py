#include <cstdio>
#include <iostream>
using namespace std;

long long first( long long N, long long m)
{
	//cout << N << " " << m << " ";
	long long ret = 1;
	while ( N-- && m)
	{
		long long base = 1LL << N;
		ret += base;
		if ( m & 1)
		{
			m >>= 1;
		}
		else
		{
			m >>= 1;
			--m;
		}
	}
	//cout << ret << endl;

	return ret;
}

long long second( long long N, long long m)
{
	long long ret = 1;
	//cout << N << " " << m << " " << endl;
	while ( N && ( m != ( ( 1LL << N) - 1)))
	{
		--N;
		if ( m & 1)
		{
			++ret;
			++m;
		}
		m >>= 1;
	}
	//cout << ret << " " << N << endl;
	//cout << m << endl;
	return ret + m;
	/*
	int j = N - 1;
	while ( m & ( 1LL << j))
	{
		--j;
	}
	long long ret = 1 << j;
	while ( j >= 0)
	{
		if ( m & ( 1LL << j))
		{
			++ret;
		}
		--j;
	}

	return ret;
	*/
}

long long calcu( long long N, long long P, long long (* method)( long long N, long long m))
{
	long long left = 0, right = 1LL << N;
	while ( left < right - 1)
	{
		long long mid = ( left + right) >> 1;

		if ( method( N, mid) > P)
		{
			right = mid;
		}
		else
		{
			left = mid;
		}
	}

	return left;
}

int main()
{
	int Tcases;
	scanf("%d", &Tcases);
	for ( int cases( 0); cases < Tcases; cases++)
	{
		long long N, P;
		scanf("%lld %lld", &N, &P);

		printf("Case #%d: %lld %lld\n", cases+1, calcu( N, P, first), calcu( N, P, second));
	}

	return 0;
}
