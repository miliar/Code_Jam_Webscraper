#include <bits/stdc++.h>
using namespace std;

int T, N, J;

int main() {
	if(fopen("test.in","r")) {
		freopen("test.in", "r", stdin);
		freopen("test.out", "w", stdout);
	}
	cin >> T;
	for(int t=1; t<=T; ++t) {
		cin >> N >> J;
		cout << "Case #" << t << ": \n";
		for(int j=0; j<J; ++j) {
			cout << "11";
			int x = j;
			for(int n=0; n<N/2-2; ++n) {
				cout << (x&1 ? "11" : "00");
				x >>= 1;
			}
			cout << "11";
			for(int k=2; k<=10; ++k) cout << " " << k+1;
			cout << '\n';
		}
	}
}
