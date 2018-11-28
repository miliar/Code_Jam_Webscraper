#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <stack>

using namespace std;

typedef long long ll;

ll getFirst(ll n, ll p)
{
	ll cur = (1LL << n), pw = 0;

	if(cur == p)
		return cur - 1;

	cur /= 2;

	for(ll cp = 1; cp <= p; cp += cur, cur /= 2) {
		++pw;
	}

	ll res = (1LL << pw) - 2;

	return res;
}

ll getSecond(ll n, ll p)
{
	ll cur = (1LL << n), res = 0;

	for(ll cp = 1, mod = 1; cp <= p; cur /= 2, cp += mod, mod *= 2) {
		if(cp != 1)
			res += cur;
	}

	return res;
}

void solve()
{
	ll n, p;
	cin >> n >> p;

	cout << getFirst(n, p) << " " << getSecond(n, p) << endl;
}

int main() {
	int n;
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}


}