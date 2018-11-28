#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<queue>
#include<stack>
#include<list>
#include<string>
#include<cstring>
#include<cstdlib>
#include<set>
#include<map>
#include<vector>
using namespace std;

typedef __int64 i64;
int test_case;
i64 A,B;
vector< i64 > palindromeSquare;

i64 makePalindrome( i64 b, int d ) {
	i64 ret = b;
	if( d % 2 ) b /= 10;
	while( b > 0 ) {
		int md = b % 10;
		ret *= 10;
		ret += md;
		b /= 10;
	}

	return ret;
}

int findLow( i64 n ) {
	int lo = 0;
	int hi = palindromeSquare.size() - 1;
	int md;
	int ans = -1;
	while( lo <= hi ) {
		md = ( lo + hi ) / 2;
		if( palindromeSquare[ md ] >= n ) {
			hi = md - 1;
			ans = md;
		} else {
			lo = md + 1;
		}
	}

	return ans;
}

bool isPalindrome( i64 n ) {
	int digits[ 20 ];
	int cnt = 0;
	while( n > 0 ) {
		digits[ cnt ++ ] = n % 10;
		n /= 10;
	}

	for( int i = 0; i < cnt / 2; i ++ ) {
		if( digits[ i ] != digits[ cnt - 1 - i ] ) return false;
	}

	
	return true;
}

void generatePalindromeSquare() {
	int i, j;
	for( i = 1; i <= 7; i ++ ) {
		int significantDigit = ceil( ( double ) ( i ) / 2.0 ) ;
		i64 offsetValue = 1;
		for( j = 0; j < significantDigit - 1; j ++ ) offsetValue *= 10;
		int numberCount = 9 * offsetValue;
		for( j = 1; j <= numberCount; j ++ ) {
			i64 baseNum = (i64) j + offsetValue - 1;
			i64 palindromeNumber = makePalindrome( baseNum, i );
			if( isPalindrome( palindromeNumber * palindromeNumber) ){
				palindromeSquare.push_back( palindromeNumber * palindromeNumber ); 
			}
		}
	
	}
}

int findHigh( i64 n ) {
	int lo = 0;
	int hi = palindromeSquare.size() - 1;
	int md;
	int ans = -1;
	while( lo <= hi ) {
		md = ( lo + hi ) / 2;
		if( palindromeSquare[ md ] <= n ) {
			lo = md + 1;
			ans = md;
		} else {
			hi = md - 1;
		}
	}

	return ans;
}

int main(){
	freopen("C-large-1.in", "r", stdin);
	freopen("outputC_Large1.txt", "w", stdout);
	generatePalindromeSquare();
	scanf("%d", &test_case);
	for( int caseId = 1; caseId <= test_case; caseId ++ ) {
		scanf("%I64d %I64d", &A, &B);
		bool ok = true;
		int lowPosition = findLow( A );
		if( lowPosition == -1 ) ok = false;
		int highPosition = findHigh( B );
		if( highPosition == -1 ) ok = false;
		int ans = highPosition - lowPosition + 1;
		if( ans <= 0 ) ans = 0;
		printf("Case #%d: %d\n", caseId, ans);
	}
	return 0;
}