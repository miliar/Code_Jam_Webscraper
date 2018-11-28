#include <cstdio>
#include <time.h>
#include <cstdlib>
#include <random>
#include <iostream>
using namespace std;

int main(void)
{
	int N = 32;
	int J = 500;
	
	int out = 0;
	cout << "Case #1: " << endl;
	for ( int c = 1; c < N-1; c += 2 )
	{
		for ( int d = 2; d <= N-2; d += 2 )
		{
			cout << "1";
			for (int e = 1; e <= N-2; e++ )
			{
				if ( e == c || e == d ){ cout << "1"; }
				else { cout << "0"; }
			}
			cout <<"1 3 2 5 2 7 2 9 2 11" << endl;
			out++;
		}
	}
	
	for ( int c = 1; c < N-1; c += 2 )
	{
		for ( int d = c+2; d < N-1; d += 2 )
		{
			for ( int c1 = 2; c1 < N-1; c1 += 2 )
			{
				for ( int d1 = c1+2; d1 < N-1; d1 += 2 )
				{
			
					cout << "1";
					for (int e = 1; e <= N-2; e++ )
					{
						if ( e == c || e == d || e == c1 || e == d1 ){ cout << "1"; }
						else { cout << "0"; }
					}
					cout <<"1 3 2 5 2 7 2 9 2 11" << endl;
					out++; if ( out == J ){ return 0; }
					
				}
			}
		}
	}
	
	
	
	
	return 0;
}