#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <stack>

using namespace std;

typedef long long ll;

const ll MOD = 1000002013;

ll getOne(ll u, ll v, ll n)
{
	assert(u <= v);

	ll k = (v - u);

	ll left = k * n;
	ll right = k * (k - 1) / 2;
	ll res = left - right;

	res %= MOD;
	res += MOD;
	res %= MOD;

	return res;
}

void solve()
{
	ll n;
	cin >> n;
	int m;
	cin >> m;

	map < ll, ll > in, out;
	set < ll > interest;

	ll totalNeed = 0, totalOptimal = 0;

	for(int i = 0; i < m; i++) {
		int from, to;
		ll howMuch;
		cin >> from >> to >> howMuch;
		in[from] += howMuch;
		out[to] += howMuch;
		interest.insert(from);
		interest.insert(to);

		totalNeed += getOne(from, to, n) * howMuch;
		totalNeed %= MOD;
	}

	typedef pair < ll, ll > person_t;

	stack < person_t > q;

	for(set < ll > :: iterator it = interest.begin(); it != interest.end(); ++it) {
		const ll x = *it;

		if(in[x] > 0) {
			q.push(person_t(x, in[x]));
		}

		if(out[x] > 0) {
			ll remain = out[x];

			while(remain > 0) {
				assert(!q.empty());
				person_t cur = q.top(); q.pop();

				ll remove = min(cur.second, remain);

				totalOptimal += getOne(cur.first, x, n) * remove;
				totalOptimal %= MOD;

				remain -= remove;
				cur.second -= remove;

				if(cur.second > 0)
					q.push(cur);
			}
		}
	}

	ll res = totalNeed - totalOptimal;
	res %= MOD;
	res += MOD;
	res %= MOD;

	cout << res << endl;
}

int main() {
	int n;
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}


}