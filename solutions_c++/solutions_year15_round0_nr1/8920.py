#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<string>
#include<queue>
#include<algorithm>
#include<iomanip>
#include<bitset>

using namespace std;


int main()
{
	freopen ( "input.txt" , "r" , stdin );
	freopen ( "output.txt" , "w" , stdout );
	int T;
	cin >> T;
	for ( int i = 0 ; i < T ; i++ )
	{
		int n;
		cin >> n;
		vector < int > vec ( n + 1 );
		for ( int i = 0 ; i < n + 1 ; i++ )
		{
			char ch;
			cin >> ch;
			vec [ i ] = ch - '0';
		}
		int sum = 0;
		int ans = 0;
		for ( int i = 0 ; i < n + 1 ; i++ )
			if( sum >= i )
				sum += vec[ i ];
			else
			{
				while ( sum < i )
					ans++ , sum++;
				sum += vec [ i ];
			}
		printf ( "Case #%d: %d\n" , i + 1 , ans );

	}
	

	
}