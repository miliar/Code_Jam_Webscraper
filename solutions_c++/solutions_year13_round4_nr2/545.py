#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;

typedef long long LL ;

int T;
int nCase = 1;

LL N, P ;

LL solv_r(LL x) 
{
	int cnt = 0;
	for ( int i=0;i<N;++i ) {
		if ( x&1LL ) ++ cnt ;
		else cnt = 0;
		x >>= 1 ;
	}
	LL ans = 0;
	for ( int i=0;i<cnt;++i ) ans = (ans+1)*2 ;
	return ans ;
}

void solv()
{
	LL num = (1LL<<N);
	if ( num == P ) cout << P-1 << " " << P-1 << endl;
	else {
	LL y = solv_r(P-1);
	LL z = num - solv_r(num-P-1)-2 ;
	cout << y << ' ' << z << endl;
	// cout << solv_r(P-1) << " " << num - solv_r(num-P-1) << endl;

	}
}
int main()
{
	cin >> T;
	while ( T -- > 0 ) {
		cin >> N >> P ;
		cout << "Case #" << nCase++ << ": " ;
		solv() ;
	}
	return 0;
}
