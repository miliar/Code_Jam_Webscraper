#include <iostream>
#include <bitset>
using namespace std;

int main() {
	int t; cin >> t;
	for(int tloop = 1; tloop <= t; ++tloop) {
		long long n; cin >> n;
	
		bitset<10> check; 
		long long i = 1;
		long long tmp;
		for(i = 1; n != 0; ++i) {
			tmp = n * i;
			while(true) {
				check.set(tmp % 10);
				tmp = tmp / 10;
				if ( tmp == 0 ) break;
			}
			if( check.all() ) break;
		}
		if(n == 0) cout << "Case #" << tloop << ": INSOMNIA" << endl;
		else       cout << "Case #" << tloop << ": " << n * i << endl;
	}
}

