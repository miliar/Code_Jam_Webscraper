#include <iostream>
#include <string>
using namespace std;

const int NV = (1<<10) - 1;

int main()
{
	string p;
	long long int T,N,M,n;
	cin >> T;
	int notvisited = NV;
	for( int i = 0 ; i < T ; i++ )
	{
		notvisited = NV;
		cin >> N ; 
		M = N;
		if( N != 0 )
			while( notvisited )
			{
				n = M;
				while( n > 0 )
				{	
					notvisited &= ~(1 << (n%10) );
					n /= 10;
				}
				M += N;
			}
		M -= N;
		if( !notvisited )
			cout << "Case #" << (i+1) << ": " << M << endl;
		else
			cout << "Case #" << (i+1) << ": " << "INSOMNIA" << endl;
	}
	return 0;
}
