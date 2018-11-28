#include <bits/stdc++.h>
using namespace std;

using ll = long long int;

int main() {
	ll t, n, cs = 0, ha, rem, hand;
	set < ll > st;
	cin >> t;
	while( t-- && cin >> n ) {
		cout << "Case #" << ++cs << ": "; 
		if( !n ) {
			cout << "INSOMNIA\n";
		} else {
			st.clear();
			ha = 0;
			do {
				ha += n;
				hand = ha;
				while( hand ) {
					st.insert( hand % 10ll );
					hand /= 10;
				}
			} while( st.size() < 10 );
			cout << ha << "\n"; 
		}
	}
    return 0;
}

