#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std ;

int t , x , y , n1 ;

int arr[4] , arr2[4] , countt ;

string str ;

int main ()
{
	freopen("A-small-attempt0.in", "r", stdin);

	freopen ("out.txt" , "w" , stdout ) ;

	cin >> t ;

	for ( int i = 1 ; i <= t ; ++i )
	{
		for ( int ii = 0 ; ii < 2 ; ++ii )
		{

			cin >> x ;

			for ( int j = 1 ; j <= 4 ; ++j )
			{
				for ( int jj = 0 ; jj < 4 ; ++jj )
				{
					if ( j == x )
					{
						if ( ii == 0 )
							cin >> arr[jj] ;
						else
							cin >> arr2[jj] ;
					}

					else
						cin >> y ;
				} 
			}

		}

		countt = 0 ;

		for ( int j = 0 ; j < 4 ; ++j )
		{
			if ( countt > 1 )
				break ;

			for ( int jj = 0 ; jj < 4 ; ++jj )
			{
				if ( arr[j] == arr2[jj] )
				{
					++countt ;

					n1 = arr[j] ;

					break ;
				}
			}
		}

		if ( countt == 0 )
			cout << "Case #" << i << ": " << "Volunteer cheated!" << endl ;
		
		else if ( countt == 1 )
			cout << "Case #" << i << ": " << n1 << endl ;
		
		else
			cout << "Case #" << i << ": " << "Bad magician!" << endl ;
	}
}