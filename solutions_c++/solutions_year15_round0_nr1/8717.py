#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for( int i=0; i<T; i++ )
	{
		int S, num=0;
		cin >> S;

		char Shyness[S+1];
		cin >> Shyness;

		int people_needed   = 0;
		int sum 	    = 0;

		for( int j = 0; j <= S; j++ )
		{	
			people_needed = max( people_needed, j - sum );
			sum += Shyness[ j ] - '0';
		}

		cout << "Case #" << i+1 << ": " << people_needed << "\n";
	}
}

