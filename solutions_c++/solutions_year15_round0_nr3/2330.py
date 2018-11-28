#include <bits/stdc++.h>
using namespace std;

#define rep(i,from,to) for (int i = from; i < to; ++i)
#define sz(x) (int)x.size()
#define trav(a, x) for (auto& a : x)
typedef long long ll;

struct Quat {
	int x;
	Quat() : x(1) {}
	static Quat fromi(int x) { Quat q; q.x = x; return q; }
	static Quat from(char c) { return fromi(c - 'g'); }
};
Quat operator*(Quat a, Quat b) {
	int ax = a.x, bx = b.x;
	bool neg = (ax < 0) ^ (bx < 0);
	if (ax < 0) ax = -ax;
	if (bx < 0) bx = -bx;
	neg ^= (ax != 1 && bx != 1 && (ax == bx || bx == ax % 3 + 2));
	int cx;
	if (ax == 1) cx = bx;
	else if (bx == 1) cx = ax;
	else if (ax == bx) cx = 1;
	else cx = 9-ax-bx;
	return Quat::fromi(neg ? -cx : cx);
}

Quat pw(Quat a, ll e) {
	if (e == 0) return Quat();
	Quat x = pw(a, e >> 1);
	x = x * x;
	if (e & 1)
		x = x * a;
	return x;
}

bool solve() {
	ll _, X;
	string str, s;
	cin >> _ >> X >> str;
	rep(i,0,(int)min(20LL,X))
		s += str;
	Quat q;
	int step = 0;
	int i = 0;
	while (i < sz(s) && step < 2) {
		q = q * Quat::from(s[i]);
		if (step == 0 && q.x == 2)
			step = 1;
		else if (step == 1 && q.x == 4)
			step = 2;
		++i;
	}
	if (step != 2) return false;
	Quat q2;
	trav(c, str)
		q2 = q2 * Quat::from(c);
	return pw(q2, X).x == -1;
}

int main() {
	int T;
	cin >> T;
	rep(i,0,T)
		cout << "Case #" << i+1 << ": " << (solve() ? "YES" : "NO") << endl;
}
