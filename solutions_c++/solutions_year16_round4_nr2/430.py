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

using flt = long double;

flt calc(const vector<flt> &p, int k, int l) {
	vector<flt> dyn(k + 1), nxt(k + 1);
	dyn[0] = 1;
	for (int ii = 0; ii < k; ++ii) {
		int i = ii < l ? ii : int(p.size()) - k + ii;
		flt q = p.at(i);
		for (int v = 0; v <= k; ++v) {
			if (v > 0)
				nxt[v] += q * dyn[v - 1];
			nxt[v] += (1 - q) * dyn[v];
		}
		swap(dyn, nxt);
		fill(all(nxt), flt(0));
	}
	return dyn[k / 2];
}

void solve() {
	vector<flt> p;
	int n, k;
	cin >> n >> k;
	p.resize(n);
	for (auto &q: p)
		cin >> q;
	sort(all(p));
	flt ans = 0;
	for (int i = 0; i <= k; ++i)
		ans = max(ans, calc(p, k, i));
	cout << fixed << setprecision(9) << ans << '\n';
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
