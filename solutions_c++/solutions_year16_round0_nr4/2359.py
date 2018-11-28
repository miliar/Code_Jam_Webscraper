#include <bits/stdc++.h>
using namespace std;

#define for_(i,a,b) for(int i=(a);i<(b);++i)
typedef long long lint;

void solve() {
	int K, C, S;
	cin >> K >> C >> S;
	for_(i,0,S) cout << i + 1 << (i < S - 1 ? " " : "\n");
}

int main() {
	int T;
	cin >> T;
	
	for_(i,0,T) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
}