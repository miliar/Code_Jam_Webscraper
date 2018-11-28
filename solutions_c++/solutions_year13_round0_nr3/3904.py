#include <cstdio>
#include <cstring>

using namespace std;

char text [1000];
bool checkPalindrome (long long num) {
	sprintf( text, "%lld", num );
	int len = strlen(text);
	for ( int a = 0; a < len/2; ++a ) {
		if ( text[a] != text[len-a-1] ) {
			return false;
		}
	}
	return true;
}

int main () {
	int TC, tc, res;
	long long a, b;
	long long n, val;
	
	scanf("%d", &TC);
	for (tc=0; tc < TC; ++tc) {
		scanf("%lld %lld", &a, &b);
		
		res = 0;
		n = 0;
		while ( true ) {
			n++;
			val = n*n;
			if ( val < a ) continue;
			if ( val > b ) break;
			if ( checkPalindrome(n) && checkPalindrome(val) ) {
				++res;
			}
			
		}
		printf("Case #%d: %d\n", tc+1, res);
	}
	return 0;
}
		
		
