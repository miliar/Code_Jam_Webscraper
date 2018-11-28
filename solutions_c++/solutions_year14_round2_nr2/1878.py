// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>
using namespace std;
#define dump(x) (cerr << #x << " = " << x << endl)
#define dump2(x, y) (cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")" << endl)
#define dump3(x, y, z) (cerr << "(" << #x << ", " << #y << ", " << #z << ") = (" << x << ", " << y << ", " << z << ")" << endl)
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
#define FOR(i, c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALL(c) (c).begin(), (c).end()
typedef pair<int, int> pii;
typedef long long ll;

int T;
const int MAX = 1010;

ll solve()
{
	int A, B, K;
	cin >> A >> B >> K;

	int cnt[MAX];
	fill(cnt, cnt+MAX, 0);

	vector<int> gen;
	REP(a, A) {
		REP(b, B)
			cnt[a&b]++;
	}
	sort(ALL(gen));
	ll ans = 0;
	REP(k, K)
		ans += cnt[k];
	return ans;
}

int main()
{
	cin >> T;
	REP(t, T) {
		printf("Case #%d: %lld\n", t+1, solve());
	}
	return 0;
}
