#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <bitset>
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
using namespace std;

typedef long long ll;

vector<ll> d;
int n, m;
vector<pair<string, vector<ll> > > sol;

ll calc(string &s, int base) {
	ll res = 0, p = 1;
	for (int i = s.size() - 1; i >= 0; --i) {
		if (s[i] == '1')
			res += p;
		p *= base;
	}
	return res;
}

void check(int msk) {
	string s = "";
	for (int temp = msk; temp != 0; temp >>= 1)
		s += char((temp & 1) + '0');
	if (s == "")
		s = "0";
	reverse(s.begin(), s.end());
	if (s.size() != n || s[0] == '0' || s[n - 1] == '0')
		return;
	d.clear();
	for (int i = 2; i <= 10; ++i) {
		ll w = calc(s, i);
		bool ok = false;
		for (ll j = 2; j*j <= w; ++j)
			if (w % j == 0) {
				d.push_back(j);
				ok = true;
				break;
			}
		if (!ok)
			return;
	}
	sol.push_back(make_pair(s, d));
}

int main(int argc, char **argv) {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, cas = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d", &n, &m);
		int from = (1 << (n - 1)) | 1;
		int to = 0;
		for (int i = 0; i < n; ++i)
			to = (to << 1) | 1;
		sol.clear();
		for (int i = from; i <= to; ++i) {
			check(i);
			if (sol.size() == m)
				break;
		}
		printf("Case #%d:\n", cas++);
		for (int i = 0; i < sol.size(); ++i) {
			printf("%s", sol[i].first.c_str());
			for (int j = 0; j < 9; ++j)
				printf(" %lld", sol[i].second[j]);
			puts("");
		}
	}
	return 0;
}