#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

#define ll long long

const int MN = 1000 * 1000 * 10;

int cnt[MN + 10];

bool is_pal(ll x) {
	vector <int> v;
	while (x) {
		v.push_back(x % 10);
		x /= 10;
	}
	int lf = 0, rg = v.size() - 1;
	while (lf <= rg) {
		if (v[lf] != v[rg])
			return false;
		lf ++, rg --;
	}
	return true;
}

int stupid(int lf, int rg) {
	int ans = 0;
	for(int i = 1; i * i <= rg; i ++) {
		if (is_pal(i) && is_pal(i * i) && i * i >= lf && i * i <= rg)
			ans ++;
	}
	return ans;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	for(int i = 1; i <= MN; i ++) {
		ll sq = (ll)i * i;
		if (is_pal(i) && is_pal(sq))
			cnt[i] ++;
		cnt[i] += cnt[i - 1];
	}
	scanf("%d\n", &t);
	for(int k = 1; k <= t; k ++) {
		ll lf, rg;
		cin >> lf >> rg;
		//int x = stupid(lf, rg);
		lf = (ll)ceil(sqrt(lf + 0.0));
		rg = (ll)floor(sqrt(rg + 0.0));
		int ans = cnt[rg];
		if (lf)
			ans -= cnt[lf - 1];
		//assert(ans == x);
		printf("Case #%d: %d\n", k, ans);
	}

	return 0;
}