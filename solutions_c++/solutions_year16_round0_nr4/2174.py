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

int main() {
	read;
	write;
	ll t, k, c, s, cs = 0;
	cin >> t;
	while (t-- && cin >> k >> c >> s) {
		printf("Case #%lld: ", ++cs);
		ll val = 1;
		rep(i, c)
			val *= k;
		if (s == 1 && val != 1) {
			puts("IMPOSSIBLE");
			continue;
		}
		else if (val == 1) {
			puts("1");
			continue;
		}
		cout << 1, s--;
		if (val - 1 != 1)
			cout << " " << val - 1, s--;
		Rep(i, 2, val + 1) if (s > 0 && i != 1 && i != val - 1)
			s--, cout << " " << i;
		else if (s <= 0)
			break;
		puts("");
	}
	return 0;
}