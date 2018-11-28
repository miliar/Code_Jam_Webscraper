#include <algorithm>
#include <iostream>
#include <set>

using namespace std;

typedef long long ll;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)

int TC;
ll A, B;

ll palin(ll i, bool midonce) {
	string ssqr = to_string(i);
	string tmp (ssqr.rbegin(), ssqr.rend());
	if (midonce) ssqr += tmp.substr(1);
	else         ssqr += tmp;
	ll fs = stoll(ssqr);
	fs *= fs;
	string pa = to_string(fs);
	int n = pa.size();
	FOR(i,0,n/2) if (pa[i] != pa[n-1-i]) return -1;
	return fs;
}

int main()
{
	ll upper = ll(10e15);
	set<ll> results;

	for (int i = 1; true; ++i) {
		ll p = palin(i, true);
		if (p > 0) results.insert(p);
		if (p > upper) break;
		p = palin(i, false);
		if (p > 0) results.insert(p);
	}
	vector<ll> res (results.begin(), results.end());

	cin >> TC;
	FOR(tc,1,TC+1) {
		cin >> A >> B;
		auto ia = lower_bound(res.begin(), res.end(), A);
		auto ib = upper_bound(res.begin(), res.end(), B);
		printf("Case #%d: %d\n", tc, int(ib - ia));
	}
}
