#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

ifstream fin( "B2.in" );
ofstream fout( "B2.out" );
#define cin fin
#define cout fout

priority_queue< int > q;
int arr[2000];

int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		while( !q.empty() )
			q.pop();
		int d, mx = 0, res = 0;
		cin >> d;
		for( int i = 0; i < d; i++ ){
			cin >> arr[i];
			res = max( res, arr[i] );
		}
		for( int a = 1; a <= 1000; a++ ){
			int s = 0;
			for( int i = 0; i < d; i++ )
				s += ( arr[i] + a - 1 ) / a - 1;
			res = min( res, s + a );
		}
		cout << "Case #" << T << ": " << res << endl;
	}

	return 0;
}