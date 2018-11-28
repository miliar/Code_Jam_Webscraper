#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

ifstream fin("A-large.in");
ofstream fout( "A2.out" );

#define cin fin
#define cout fout

int test, n, T = 1, A;
int arr[1000000];

int main()
{
	for( cin >> test; test--; ){
		cin >> A >> n;
		for( int i = 0; i < n; i++ )
			cin >> arr[i];
		sort( arr, arr + n );
		int curS = 0, res = n, br = 0;
		for( int i = 0; i < n; i++ ){
			if( A > arr[i] )
				A += arr[i];
			else{
				res = min( res, curS + n - i );
				if( A == 1 ){
					br = 1;
					break;
				}
				while( A <= arr[i] ){
					curS++;
					A = ( A + A - 1 );
				}
				A += arr[i];
			}
		}
		if( br == 0 )
			res = min( res, curS );
		cout << "Case #" << T++ << ": " << res << endl;
	}

	return 0;
}