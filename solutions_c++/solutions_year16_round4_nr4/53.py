#include <iostream>

using namespace std;

int n;

int cnt(int x) {
	return __builtin_popcount(x);
}

bool ok(int p, int m, int k) {
	if(p == (1 << n) - 1) {
		return m == (1 << n) - 1;
	}
	for(int i = 0; i < n; ++i) {
		if(p & (1 << i)) continue;
		bool found = false;
		for(int j = 0; j < n; ++j) {
			if(m & (1 << j)) continue;
			if(!(k & (1 << (n * i + j)))) continue;
			found = true;
			if(!ok(p | (1 << i), m | (1 << j), k)) return false;
		}
		if(!found) {
			if(!ok(p | (1 << i), m, k)) return false;
		}
	}
	return true;
}

int main() {
	cin.sync_with_stdio(false);
	cin.tie(nullptr);
	
	int tc;
	cin >> tc;
	for(int ti = 1; ti <= tc; ++ti) {
		cin >> n;
		
		int bk = 0;
		for(int i = 0; i < n; ++i) {
			string S;
			cin >> S;
			for(int j = 0; j < n; ++j) {
				if(S[j] == '1') {
					bk |= 1 << (n * i + j);
				}
			}
		}
		
		int asd = 100000;
		for(int k = 0; k < (1 << (n * n)); ++k) {
			if((k & bk) != bk) continue;
			if(ok(0, 0, k)) {
				asd = min(asd, cnt(k) - cnt(bk));
			}
		}
		
		cout << "Case #" << ti << ": ";
		cout << asd << '\n';
	}
	
	return 0;
}
