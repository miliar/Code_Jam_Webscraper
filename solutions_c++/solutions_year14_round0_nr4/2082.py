#include <bits/stdc++.h>
using namespace std;

double arr1[1005] , arr2[1005] ;
bool arr[1005] ;
int main()
{
	int t , k ;

	#ifndef ONLINE_JUDGE
		freopen( "in.txt" , "r" , stdin ) ;
		freopen( "out.txt" , "w" , stdout ) ;
	#endif

	cin >> t ;
	//p.get(ch);

	int n , i , j ;
	for( k = 1 ; k <= t ; k++ )
	{
		memset( arr , false , sizeof( arr ) ) ;
		cin >> n ;
		for( i = 1 ; i <= n ; i++ ) cin >> arr1[i] ;
		for( i = 1 ; i <= n ; i++ ) cin >> arr2[i] ;

		sort( arr1 + 1 , arr1 + n + 1 ) ;
		sort( arr2 + 1 , arr2 + n + 1 ) ;

		i = 1 ; j = n ;

		cout << "Case #" << k << ": " ;
		//deciteful war ....

		int last = n ;
		for( i = 1 ; i <= n ; i++ ) {
            for( j = 1 ; j <= last ; j++ ) {
                if( !arr[j] && arr1[i] > arr2[j] ) {
                    arr[j] = true ; break ;
                }
            }
            if( j == last+1 ) {  last-- ; }

		}
		j = 0 ;
		for( i = 1 ; i <= n ; i++ ) if( arr[i] ) j++ ;

		cout << j ;

        memset( arr , false , sizeof( arr ) ) ;
		for( i = 1 ; i <= n ; i++ ) {
			for( j = 1 ; j <= n ; j++ ) {
				if( ( arr1[i] < arr2[j] ) && ( !arr[j] ) ) { arr[j] = true ; break ;}
			}
		}

		j = 0 ;
		for( i = 1 ; i <= n ; i++ ) if( !arr[i] ) j++ ;
		cout << " " << j << endl ;

	}

	return 0;
}
