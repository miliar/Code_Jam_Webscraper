#include <bits/stdc++.h>
using namespace std;
#if defined(ILIKEGENTOO)
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')
#else
#define E($...) ;
#endif
#define all(x) begin(x), end(x)
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(nullptr);}}$;


string build(int n, int ind, int v) {
	if (ind * 2 >= (1 << (1 + n))) {
		return string(1, "PRS"[v]);
	}
	string l = build(n, ind * 2, v);
	string r = build(n, ind * 2 + 1, (v + 1) % 3);
	if (l > r)
		swap(l, r);
	l += move(r);
	return l;
}

void fail() {
	cout << "IMPOSSIBLE\n";
}

void solve() {
	int n, p, r, s;
	cin >> n >> r >> p >> s;
	array<int, 3> dyn, nxt;
	fill(all(dyn), 0);
	fill(all(nxt), 0);
	dyn[0] = 1;
	int unt = 0;
	for (int i = 0; i < n; ++i) {
		nxt[0] = dyn[2] + dyn[0];
		nxt[1] = dyn[0] + dyn[1];
		nxt[2] = dyn[1] + dyn[2];
		dyn = nxt;
		unt = (unt + 2) % 3;
	}
	int unp;
	if (p == r)
		unp = 2;
	else if (p == s)
		unp = 1;
	else
		unp = 0;
	int rot = (3 - unp + unt) % 3;
	//E(unt, unp, rot);
	rotate(begin(dyn), begin(dyn) + rot, end(dyn));
	if (dyn[0] != p || dyn[1] != r || dyn[2] != s)
		return fail();
	string ans = build(n, 1, (3 - rot) % 3);
	cout << ans << '\n';
}

int main() {
	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ++ti) {
		cout << "Case #" << ti << ": ";
		solve();
	}
	return 0;
}
