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

typedef long double flt;
const flt eps = 1e-8;
flt V, C;

struct Pipe {
	flt c, r;
};

bool operator<(const Pipe &a, const Pipe &b) {
	return a.c < b.c;
}

vector<Pipe> pipes;

flt ans = -1;

void calc() {
	//E(V, C); for (const auto &P: pipes) E(P.r, P.c);
	Pipe sum;
	sum.c = sum.r = 0;
	for (const auto &p: pipes) {
		assert(sum.c != p.c);
		flt x0 = -1, x1 = -1, tim;
		if (sum.r > 0) {
			x0 = V * (C - p.c) / (sum.c - p.c);
			x1 = V - x0;
		} else if (p.c == C) {
			x0 = 0;
			x1 = V;
		}
		if (x0 < -eps || x1 < -eps)
			goto end;
		x0 = max(x0, flt(0)); x1 = max(x1, flt(0));
		tim = x1 / p.r;
		//E(x0, x1); E(sum.r, sum.c, p.r, p.c);
		if (x0 > 0) {
			assert(sum.r > 0);
			tim = max(x0 / sum.r, tim);
		}
		assert(tim > 0);
		if (ans < 0 || tim < ans)
			ans = tim;

end:;
		sum.c = (sum.c * sum.r + p.c * p.r) / (sum.r + p.r);
		sum.r = (sum.r + p.r);
	}
}

void solve() {
	int n;
	cin >> n >> V >> C;
	pipes.clear();
	ans = -1;
	for (int i = 0; i < n; ++i) {
		Pipe p;
		cin >> p.r >> p.c;
		auto it = lower_bound(all(pipes), p);
		if (it != end(pipes) && it->c == p.c) {
			it->r += p.r;
		} else {
			pipes.insert(it, p);
		}
	}
	calc();
	reverse(all(pipes));
	calc();
	if (ans < 0)
		cout << "IMPOSSIBLE";
	else
		cout << fixed << setprecision(9) << ans;
}

int main() {
	int tcase;
	cin >> tcase;
	for (int t = 0; t < tcase; ++t) {
		cout << "Case #" << (t + 1) << ": ";
		solve();
		cout << "\n";
	}
	return 0;
}

