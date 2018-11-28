#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>


using namespace std;

int T;
long long  A,B,a,b;

bool is_loop ( const int& number)
{

	int sum = 0,x = number;
	while( x )
	{
		sum = 10*sum + x%10;
		x /= 10;
	}
	return sum == number;
}

void gcj(const int& count)
{
	long long temp;
	int number = 0;
	for( long long i = a; i <= b; ++i )
	{
		if( !is_loop(i) )
			 continue;
		temp = i * i;
		if( is_loop(temp) &&  temp >= A && temp <= B )
			number++;

	}

	cout << "Case #" << count <<": " << number << endl;
}


int main()
{

    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
	cin >> T;
	for( int count = 1; count <= T; ++count )
	{
		cin >> A >> B;
		a = ceil(sqrt(A));
		b = floor(sqrt(B));
		// cout << a << b;
		gcj(count);
	}
	return 0;
}
