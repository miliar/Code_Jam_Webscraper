#include "iostream"
#include "string"
#include "vector"
#include "algorithm"

using namespace std;

struct Solution {
	vector<bool> p;

	void invert(int i) {
		int b = 0, e = i;
		while (b < e) swap(p[b++], p[e--]); // swap
		for (b = 0; b <= i; b++) p[b] = !p[b]; // invert
	}

	int force(bool value, int i) {
		if (i < 0) return 0;
		if (p[i] == value) return force(value, i-1);
		else if (p[0] != value) {
			invert(i);
			return force(value, i - 1)+1;
		}
		else if (p[0] == value) {
			int j = i; // save i
			while (p[i] != value) i--; // ignore wrong values at the end
			int moves = force(!value, i);
			invert(j);
			return moves+1;
		}
		throw exception();
	}
	
	void solve() {
		cout << force(true, p.size() - 1);
	}
}
;
int main() {
	int T = 0;
	cin >> T;

	for (int t = 0; t < T; t++) {
		string ps;
		cin >> ps;
		vector<bool> p(ps.size());
		for (int i = 0; i < ps.size(); i++) if (ps[i] == '+') p[i] = true;
		cout << "Case #" << t + 1 << ": ";
		Solution{ p }.solve();
		
		cout << endl;
	}

	return 0;
}