#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;


int x[1001],y[1001];

int isPalindrome(int a)
{
	int r = 0, t;
	t = a;
	while (t)
	{
		r = r*10 + t%10;
		t /= 10;
	}
	return (r==a);
}

void calc()
{
	int k;
	for ( int i = 1; i <= 1000; ++i )
	{
		x[i] = isPalindrome(i);
	}

	for ( int i = 1; i <= 1000; ++i )
	{
		if ( x[i] )
		{
			k = int(sqrt(i));
			
			if ( k*k == i && x[k] )
				y[i] = 1;
		}
	}
}

int main()
{
	int t, a, b, c;
	calc();
	cin >> t;
	for ( int i = 1; i <= t; ++i )
	{
		cin >> a >> b;
		c = 0;
		for (int j = a; j <= b; ++j )
		{
			if (y[j])
			{
				++c;
			}
		}
		printf ("Case #%d: %d\n", i, c);
	}
	return 0;
}
