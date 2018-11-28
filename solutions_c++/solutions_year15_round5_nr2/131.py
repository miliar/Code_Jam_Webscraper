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

int n, k;
vector<int64_t> sum;
vector<int64_t> cur, mx, mn;

void solve() {
	cin >> n >> k;
	sum.resize(n - k + 1);
	for (auto &s: sum)
		cin >> s;
	cur.assign(k, 0);
	mx.assign(k, 0);
	mn.assign(k, 0);
	for (int i = k; i < n; ++i) {
		int64_t d = sum[i - k + 1] - sum[i - k];
		int ind = i % k;
		cur[ind] += d;
		mx[ind] = max(mx[ind], cur[ind]);
		mn[ind] = min(mn[ind], cur[ind]);
	}
	int64_t mxdf = mx[0] - mn[0];
	for (int i = 1; i< k; ++i)
		mxdf = max(mxdf, mx[i] - mn[i]);
	int64_t left = 0, r = 0;
	for (int i = 0; i < k; ++i) {
		int64_t d = -mn[i];
		r += d;
		left += mxdf - (mx[i] + d);
	}

	int64_t s0 = sum[0] - r;
	s0 %= k;
	if (s0 < 0) s0 += k;
	assert(s0 >= 0);
	assert(left >= 0);
	if (s0 > left)
		++mxdf;
	cout << mxdf;
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

