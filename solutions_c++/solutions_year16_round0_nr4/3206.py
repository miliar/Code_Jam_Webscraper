#include <iostream>
#include <algorithm>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

int T;
long long k, c, s;

int main(){
	
	optimizar_io
	cin >> T;
	for( int t = 1; t <= T; t++ ){
		cin >> k >> c >> s;
		cout << "Case #" << t << ":";
		c--;
		for( long long i = 0; i < k; i++ ){
			long long p = i;
			for( long long j = 0; j < c; j++ ){
				p *= k;
				p += i;
			}
			cout << " " << p + 1;
		}
		cout << "\n";
	}
	return 0;
	
}