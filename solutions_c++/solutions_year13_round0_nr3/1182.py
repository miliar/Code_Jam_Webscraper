#include <iostream>
#include <fstream>

using namespace std;

ifstream fin( "C-large-1.in" );
ofstream fout( "C2.out" );
#define cin fin
#define cout fout

long long arr[10000000];
int tot = 0;

bool isPal( long long n ){
	int arr[20], ptr = 0;
	while( n )
		arr[ptr++] = n % 10, n /= 10;
	for( int i = 0; i < ptr; i++ )
		if( arr[i] != arr[ptr - i - 1] )
			return false;
	return true;
}

int test, T = 1;
long long A, B;

int main()
{
	for( long long i = 1; i <= 10000000; i++ )
		if( isPal( i ) && isPal( i * i ) )
			arr[tot++] = i * i;
	//cout << tot << endl;
	for( cin >> test; test--; ){
		cin >> A >> B;
		int res = 0;
		for( int i = 0; i < tot; i++ )
			if( arr[i] >= A && arr[i] <= B ){
				res++;
			}
		cout << "Case #" << T++ << ": " << res << endl;
	}
	return 0;
}