#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <sstream>
#include <assert.h>
#include <set>
#include <map>
#include <math.h>
#include <queue>
#include <utility>
#include <time.h>
#include <limits.h>
#include <string.h>
using namespace std;

long long getNextPalim(long long a)
{
	char astr[1024];
	sprintf(astr, "%lld", a );
	int alen = strlen(astr);

	long long U = 0;
	long long D = 0;
	long long Ubase = 1;
	bool all9 = true;
	for( int i = 0; i < (alen+1)/2; i ++ ){
		U = U * 10 + astr[i] - '0';
		if( astr[i] != '9' )
			all9 = false;
	}
	for( int i = (alen+1)/2; i < alen; i ++ )
		Ubase *= 10;
	for( int i = alen/2-1; i >= 0; i -- )  D = D * 10 + astr[i] - '0';
	long long P0 = U * Ubase + D;
	if( a < P0 ) return P0;
	if( all9 ) return P0 + 2;

	sprintf(astr, "%lld", U+1 );
	long long D1 = 0;
	for( int i = alen/2-1; i >= 0; i -- )  D1 = D1 * 10 + astr[i] - '0';
	long long P1 = (U+1) * Ubase + D1;
	return P1;
}
bool isPalim( long long a ) {
	return a < 10 || getNextPalim(a-1) == a;
}

int main(void)
{
	int N;
	cin >> N;

	for( int C = 1; C <= N; C ++ ){
		long long A, B;
		cin >> A >> B;
		long long r = (long long)sqrt((long double)A)-2;
		long long c = 0;
		if( r <= 0 ) r = 1;
		while( r * r < A) r = getNextPalim(r);
		while( r * r <= B){
			if( isPalim(r*r) ){
//				cerr << r*r << endl;
				c ++;
			}
			r = getNextPalim(r);
		}
		cout << "Case #" << C << ": " << c << endl;
	}
	return 0;
}
