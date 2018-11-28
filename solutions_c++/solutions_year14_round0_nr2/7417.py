#include <iostream>
using namespace std;

double c, f, s, x, cur;
int TC;

int main() {
	cin >> TC;
	for( int cas = 1; cas <= TC; cas++ ) {
		cin >> c >> f >> x;
		cur = 2;
		s = 0;
		while( x / cur > c / cur + x / (cur + f) ) {
			s += c / cur;
			cur += f;
		}
		s += x / cur;
		printf( "Case #%d: %.7f\n", cas, s );
	}
	// your code goes here
	return 0;
}