#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
void PR(vi &v) { trav(x, v) cout << x << ' '; cout << endl; }

void solve() {
	int N, K;
	cin >> N >> K;
	vector<double> prob(N);
	rep(i,0,N) cin >> prob[i];
	sort(all(prob));
	vector<double> dp(1, 1.0), ndp;
	double e = 0;
	auto addp = [&](double p) {
		e += p;
		ndp = dp;
		dp.push_back(0.0);
		ndp.insert(ndp.begin(), 0.0);
		trav(x, dp) x *= 1-p;
		trav(x, ndp) x *= p;
		rep(j,0,sz(dp)) dp[j] += ndp[j];
	};

	double res = 0;

	rep(i,0,K+1) {
		dp.assign(1, 1.0);
		rep(k,0,i) addp(prob[k]);
		rep(k,0,K-i) addp(prob[N-1-k]);
		res = max(res, dp[K/2]);
	}

	/*
	int i = 0, j = N;
	rep(t,0,K) {
		double p1 = prob[i], p2 = prob[j-1];
		int incl = i + N-j;
		if (e / incl < 0.5) addp(p2), j--;
		else addp(p1), i++;
	}
	*/

	/*
	int i = 0;
	while (i < K/2) {
		if (prob[i] >= 0.5 || prob[N-1-i] <= 0.5) break;
		addp(prob[i]);
		addp(prob[N-1-i]);
		i++;
	}
	if (i < K/2) {
		cout << -1 << endl; return;
	}
	*/

	cout << setprecision(10) << fixed << res << endl;
}

int main() {
	cin.sync_with_stdio(false);
	cin.tie(0);
	int N;
	cin >> N;
	rep(i,0,N) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}
