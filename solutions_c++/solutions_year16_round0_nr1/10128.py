#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;

bool pass  ( int *arr) {
	int i;
	for ( i = 0; i < 10; ++i ) {
		if ( arr[i] == 0 ) return false;
	}
	return true;
}
void process ( long long int init, long long int n, int *arr, int test, int num) {
	long long int copy = n;
	//printf ( "%i\n", copy );
	while ( n != 0 ) {
		int index = n%10; 
		n /= 10;
		arr[index] = 1;
		if ( pass ( arr) ) {
			cout <<"Case #" << test <<": "<< copy <<"\n";
			return;
		}
	}
	num += 1;
	process ( init, init*num, arr, test, num);
}

int main ( void ) {
	int t; int i = 1;
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
		long long int n; string s;
		//getline ( cin, s ) ;
		getline ( cin, s );
		cin >> n;
		//getline ( cin, s );
		while ( getline ( cin, s ) )  {
			//cin >> n;
			//if (s == "" || s == "\n") continue;
		//n = static_cast<int>(s[0]); 
		//cout << n << endl;
		int *arr = ( int * ) malloc ( sizeof ( int ) * 10 );
		memset ( arr, 0, sizeof ( arr ));
		//process ( 1692, 1692, arr, 1, 1 );
		if ( n == 0 ) 
			cout << "Case #"<<i<<": INSOMNIA\n";
		else {
			process ( n, n, arr, i, 0 );
		}
		i += 1;
		
		cin >> n;

	}
}