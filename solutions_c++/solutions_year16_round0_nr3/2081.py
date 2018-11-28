#include <iostream>
#include <string>
#include <cstring>
#include <map>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

#define FOR(i, a, b) for(int i = a; i <= b; i++)

int n = 16;
vector<string> ans;
const int M = 1000000;
int b[M], p[M];
int o = 0;

int pr(long long n) {
	if (n < M && !b[n]) return 0;
	FOR(i, 0, o - 1) 
		if (n % p[i] == 0)
			return p[i];
	return 0;
}

long long power[15][17];

bool ok(string s) {
	reverse(s.begin(), s.end());
	vector<int> qq;
	FOR(k, 2, 10) {
		long long tmp = 0;
		for (int i = 0; i < n; i++)
			if (s[i] == '1')
				tmp += power[k][i];
		int res = pr(tmp);
		if (!res)
			return false;
		qq.push_back(res);
	}
	reverse(s.begin(), s.end());
	cout << s << s;
	FOR(i, 0, qq.size() - 1)
		cout << ' ' << qq[i];
	cout << endl;
	static int count = 0;
	cerr << ++count << "   ";
	cerr << s << s;
	FOR(i, 0, qq.size() - 1)
		cerr << ' ' << qq[i];
	cerr << endl;
	return true;
}

int main() {
	FOR(i, 2, M - 1)
		if (!b[i]) {
			p[o++] = i;
			FOR(j, 2, (M - 1) / i)
				b[j * i] = 1;
		}
	FOR(k, 2, 10) {
		power[k][0] = 1;
		FOR(i, 1, n)
			power[k][i] = power[k][i - 1] * k;
	}
	cout << "Case #1:" << endl;
	for (int msk = (1 << (n - 1)) + 1; msk < (1 << n) && ans.size() < 500; msk += 2) {
		string s;
		FOR(i, 0, n - 1)
			if (msk >> i & 1)
				s += '1';
			else
				s += '0';
		if (ok(s))
			ans.push_back(s);
	}
}