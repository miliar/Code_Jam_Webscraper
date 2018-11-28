#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <queue>
using namespace std;
const int MAXN = 100 + 10;

string s;
char cmax, cmin;
int len;

int main() {
	freopen( "A.out", "w+", stdout );
	int t;
	cin >> t;
	for( int ncas = 1; ncas <= t; ++ncas ) {
		deque<char> deq;
		deque<char>::iterator it;
		cout << "Case #" << ncas << ": ";
		cin >> s;
		len = s.length();
		string ans( len, ' ' );
		cmax = cmin = s[0]; deq.push_back( s[0] );
		for( int i = 1; i < len; ++i ) {
			if( s[i] >= cmax ) {
				deq.push_front( s[i] );
				cmax = s[i];
			} else { deq.push_back( s[i] ); }
		}
		int i = 0;
		for( it = deq.begin(); it != deq.end(); ++it, ++i ) {
			ans[i] = *it;
		}
		cout << ans << endl;
	}
	return 0;
}
