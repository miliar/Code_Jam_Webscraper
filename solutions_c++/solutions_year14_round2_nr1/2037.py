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
const int INF = 1<<25;

int solve(int i, int j, string a, string b)
{
	if (i == 0 && a[i] != b[j]) return -INF;
	if (i == a.size() && j == b.size()) return 0;
	if (i == a.size()) {
		if (a[i-1] == b[j])
			return 1+solve(i, j+1, a, b);
		else
			return -INF;
	}
	if (j == b.size()) {
		if (b[j-1] == a[i])
			return 1+solve(i+1, j, a, b);
		else
			return -INF;
	}

	int ans = 0;
	if (a[i] != b[j]) {
		if (a[i-1] == a[i]) {
			ans += 1 + solve(i+1, j, a, b);
		} else {
			ans += 1 + solve(i, j+1, a, b);
		}
	} else {
		ans += solve(i+1, j+1, a, b);
	}
	return ans;
}

int main()
{
	cin >> T;
	REP(t, T) {
		int N;
		cin >> N;
		vector<string> vs = vector<string>(N);
		REP(i, N)
			cin >> vs[i];
		
		printf("Case #%d: ", t+1);
		int ans = solve(0, 0, vs[0], vs[1]);
		if (ans < 0)
			cout << "Fegla Won" << endl;
		else
			cout << ans << endl;
	}
	return 0;
}
