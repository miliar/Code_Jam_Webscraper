#include <bits/stdc++.h>

#define itn itn
#define all(x) (x).begin(), (x).end()
#define x first
#define y second

using namespace std;

inline int nxt(){
	int x;
	scanf("%d", &x);
	return x;
}

void solve(){
	int n = nxt();
	int k = nxt();
	vector<long long> m(k), M(k);
	long long cur = 0;
	vector<long long> a(n);
	for (int i = 0; i < n - k + 1; i++){
		if (i)
			cur -= a[i - 1];
		a[i + k - 1] = nxt() - cur;
		cur += a[i + k - 1];
		if (!i)
			m[k - 1] = M[k - 1] = a[k - 1];
		m[(i + k - 1) % k] = min(m[(i + k - 1) % k], a[i + k - 1]);
		M[(i + k - 1) % k] = max(M[(i + k - 1) % k], a[i + k - 1]);
	}
	long long sum = accumulate(all(m), 0);
	long long avg = (sum > 0) ? sum / k : -((-sum + k - 1) / k);
	long long rem = (sum > 0) ? sum % k : (k - ((-sum) % k)) % k;
	assert(avg * k + rem == sum && rem >= 0 && rem < k);
	vector<pair<long long, long long>> p(k);
	for (int i = 0; i < k; i++)
		p[i] = {m[i], M[i]};
	sort(all(p), [](const pair<long long, long long>& x, const pair<long long, long long>& y){
		return (x.y - x.x < y.y - y.x);
	});
	for (int i = 0; i < k; i++){
		p[i].y += avg - p[i].x;
		p[i].x += avg - p[i].x;
	}
	long long ans = p.back().y - p.back().x;
	long long charge = 0;
	for (int i = 0; i < k; i++)
		charge += p.back().y - p[i].y;
	if (charge < rem)
		ans++;
	printf("%lld\n", ans);
}

int main(){

	int T = nxt();
	for (int _ = 0; _ < T; _++){
		printf("Case #%d: ", _ + 1);
		solve();
		cerr << "Test #" << _ + 1 << " completed\n";
	}

	return 0;
}