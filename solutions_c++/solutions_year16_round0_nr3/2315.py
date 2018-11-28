//~In The Name Of Allah~//
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <math.h>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <string.h>
#include <sstream>
#include <fstream>
#include <functional>
#include <stack>
#include <utility> 
#include <set>
#include <list>
#include <queue>
#include <bitset>
#include <time.h>
using namespace std;

#define read freopen("in.txt", "r", stdin)
#define write freopen("out.txt", "w", stdout)
#define all(_) _.begin(), _.end()
#define rall(_) _.rbegin(), _.rend()
#define rep(i, j) for (int i = 0; i < j; i++)
#define Rep(i, j, k) for (int i = j; i < k; i++)
#define siz(_) (int)_.size()
#define ll long long
#define endl '\n'

const double PI = 2.0 * acos(0.0);
const double EX = 2.7182818284;
const int MOD = 1e9 + 7;
const int oo = 2e9 + 1e8;

ll gcd(ll x, ll y) { return !y ? x : gcd(y, x%y); }

vector<ll> ans;

ll prime(ll n) {
	for (ll i = 2; i*i <= n; i++) if (n%i == 0)
		return i;
	return 0;
}

bool good(ll n) {
	for (ll i = 2; i <= 10; i++) {
		ll bas = 1, hope = 0, tmp = n;
		while (tmp) {
			if (tmp & 1)
				hope += bas;
			bas *= i, tmp >>= 1;
		}
		ll ret = prime(hope);
		if (!ret)
			return 0;
		ans.push_back(ret);
	}
	return 1;
}

int main() {
	read;
	write;
	ll t, n, j;
	cin >> t;
	while (t-- && cin >> n >> j) {
		puts("Case #1:");
		ll opt = (1 << (n - 1)) + 1;
		while (j--) {
			while (!((opt & 1) && (opt&(1 << (n - 1)))))
				opt++;
			ll resto = opt;
			if (prime(opt) && good(opt)) {
				string str = "";
				while (opt)
					str += (opt & 1) + '0', opt >>= 1;
				reverse(all(str));
				cout << str << " ";
				rep(i, 9)
					cout << ans[i] << " ";
				puts("");
			}
			else
				j++;
			ans.clear(), opt = resto + 1;
		}
	}
	return 0;
}