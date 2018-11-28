#include <bits/stdc++.h>
using namespace std;

#define for_(i,a,b) for(int i=(a);i<(b);++i)
typedef long long lint;

lint solve() {
	lint N;
	cin >> N;
	
	set< int > set;
	
	for_(i,0,1000000) {
		lint n = (i + 1) * N;
		
		while (n > 0) {
			set.insert(n % 10);
			n /= 10;
		}
		
		if (set.size() == 10) return (i + 1) * N;
	}
	
	return -1;
}

int main() {
	int T;
	cin >> T;
	
	for_(i,0,T) {
		int ans = solve();
		cout << "Case #" << i + 1 << ": ";
		if (ans == -1) cout << "INSOMNIA" << endl;
		else cout << ans << endl;
	}
}