#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;
int test;
int arr[1000000];
bool mark[1000000];

ifstream fin( "A2.in" );
ofstream fout( "A2.out" );
#define cin fin
#define cout fout

int main()
{
	cin >> test;
	int n, x;
	for( int T = 1; T <= test; T++ ){
		memset( mark, false, sizeof mark );
		cin >> n >> x;
		for( int i = 0; i < n; i++ )
			cin >> arr[i];
		sort( arr, arr + n );
		int res = 0;
		for( int i = n - 1; i >= 0; i-- ){
			if( mark[i] )
				continue;
			int sel = 0;
			for( int j = i - 1; j >= 0; j-- ){
				if( !mark[j] && arr[i] + arr[j] <= x ){
					mark[j] = true;
					res++;
					sel = 1;
					break;
				}
			}
			if( !sel )
				res++;
		}
		cout << "Case #" << T << ": " << res << endl;
	}

	return 0;
}