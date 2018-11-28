#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for(int i = 0;i < n;++i)
#define FOR(i, a, b) for(int i = a;i < b;++i)

int x, r, c;

bool pada(int a, int b) {
	if(min(a, b) > min(r, c)) return true; 
	if(max(a, b) > max(r, c)) return true;
}

bool richard() {
	if(x == 1) return false;
	if(x == 2 && r*c == 2) return false;
	if((r * c) % x) return true;
	FOR(i, 1, x + 1) if(pada(i, x - i + 1)) return true;
	if(r >= 3 && c >= 3 && x >= 7) return true;
	if(x >= r + c - 1) return true;
	if(min(r, c) == 1 && (x > r*c/2 || x >= 3)) return true;
	if(min(r, c) == 2 && x >= 4) return true;
	if(min(r, c) == 3 && x >= 5) return true;	
	return false;
}

int main() {
	int t;
	cin >> t;
	REP(i, t) {
		cin >> x >> r >> c;
		cout << "Case #" << i + 1 << ": ";
		if(richard()) cout << "RICHARD\n";
		else cout << "GABRIEL\n";
	}
}