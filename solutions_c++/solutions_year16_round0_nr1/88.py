#include <bits/stdc++.h>
using namespace std;

int main() {
	int _;
	cin >> _;
	for(int __ = 0; __ < _; __++) {
		cout << "Case #" << __+1 << ": ";
		int n;
		cin >> n;
		if(n == 0) cout << "INSOMNIA\n";
		else {
			bool cnt[10];
			for(int d = 0; d < 10; d++) cnt[d] = 0;
			bool asleep = 0;
			int m = n;
			while(!asleep) {
				for(int t = m; t; t /= 10) {
					cnt[t%10] = 1;
				}
				asleep = 1;
				for(int d = 0; d < 10; d++)
					if(!cnt[d]) asleep = 0;
				if(asleep) 
					cout << m << "\n";
				m += n;
			}
		}
	}
	return 0;
}
