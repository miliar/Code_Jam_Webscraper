#include <cstdio>
#include <time.h>
#include <cstdlib>
#include <random>
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <iomanip>
#include <sstream>

using namespace std;

int main(void)
{
	int T;
	cin >> T;
	
	for ( int tc = 0; tc < T; tc++ )
	{
		int N;
		cin >> N;
		
		int P[N];
		
		for (int c = 0; c < N; c++)
		{
			cin >> P[c];
		}
		
		int total = 0;
		for (int c = 0; c < N; c++ )
		{
			total += P[c];
		}
		
		cout << "Case #" << tc+1 << ": "; 
		while ( total >= 2 )
		{
			int cMax = 0, cMaxIdx = 0;
			for ( int c = 0; c < N; c++ )
			{
				if ( P[c] > cMax ){ cMax = P[c]; cMaxIdx = c; }
			}
			
			P[cMaxIdx]--;
			
			int cMaxIdx2 = -1; int cMax2 = 0;
			
			for ( int c = 0; c < N; c++ )
			{
				if ( P[c] > cMax2 ){ cMax2 = P[c]; cMaxIdx2 = c; } 
			}
			if ( cMax2 <= (total-1)/2 ){ 
				total--;
				printf("%c ", (cMaxIdx+(int)'A') );
			}
			else {
				total -= 2;
				P[cMaxIdx2]--;
				printf( "%c%c ", (cMaxIdx+(int)'A'),(cMaxIdx2+(int)'A'));
			}			
		}
		cout << endl;
		
		
	}

	return 0;
}