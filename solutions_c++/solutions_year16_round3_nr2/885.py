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

long long intPow(long long B, long long E)
{
	if ( E == 0 ){ return 1; }
	if ( E == 1){ return B; }
	if ( E%2 == 1 ){ 
		return B*intPow(B*B,E/2);
	}else {
		return intPow(B*B,E/2);
	}
}

int main(void)
{
	int T;
	cin >> T;
	
	for ( int tc = 0; tc < T; tc++ )
	{
		long long B, M;
		cin >> B >> M;
		
		long long tmp1 = intPow ( 2,B-2 );
		
		if ( tmp1 < M ){ 
			cout << "Case #" << tc+1 << ": IMPOSSIBLE" << endl; 
			continue;
		}
		
		cout << "Case #" << tc+1 << ": POSSIBLE" << endl;
		
		bool binRep[B];
		for ( int c = 0; c < B; c++ ){ binRep[c] = false; }
		long long M2 = M; int curr = 0;
		while (M2 > 0 )
		{
			if ( M2 % 2 == 1 ){ binRep[curr] = true; }
			M2 /= 2;
			curr++;
		}
		
		bool matrix[B][B];
		for ( int c = 0; c < B; c++)
		{
			for ( int d = 0; d < B; d++ )
			{
				matrix[c][d] = false;
			}	 
		}
			 
		int max = 0;
		for ( int c = 0; c < B; c++ )
		{
			if ( binRep[c] ){ max = c; }
		}
		
		for ( int c = B-2; c >= B-2-max; c-- )
		{
			for ( int d = c+1; d < B; d++ )
			{
				matrix[c][d] = true;
			}
		}
		
		if ( tmp1 > M ){ 
			for ( int c = 0; c < B; c++ )
			{
				if ( binRep[c] ){
					matrix[0][B-2-c] = true;
				}
			}
		}
		
		
		for ( int c = 0; c < B; c++ )
		{
			for ( int d = 0; d < B; d++ )
			{
				if ( matrix[c][d] ){ cout << "1"; }
				else { cout << "0"; }
			}
			cout << endl;
		}
		
	}

	return 0;
}