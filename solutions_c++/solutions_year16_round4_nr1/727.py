#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

const int N = 5e5 + 200;
const int SL = 2500;
#define MP make_pair
#define lli long long int
#define y1 y123123


char iBear(char v) {
	if (v == 'R') return 'S';
	if (v == 'P') return 'R';
	return 'P';
}

int cnt[N];
int n;
int tcnt[N];
char ans[N];

bool isgreater(int l, int r) {
	int m = (l + r) / 2;
	for (int i = l, j = m + 1; i <= m; ++i, ++j) {
		if (ans[i] > ans[j]) return true;
		if (ans[i] < ans[j]) return false;
	}
	return false;
}

void myswap(int l, int r) {
	int m = (l + r) / 2;
	for (int i = l, j = m + 1; i <= m; ++i, ++j) {
		swap(ans[i], ans[j]);
	}
}

void solve(char type, int l, int r) {
	if (l == r) {
		ans[l] = type;
	}
	else {
		int m = (l + r) / 2;
		solve(type, l, m);
		solve(iBear(type), m + 1, r);
		if (isgreater(l, r)) myswap(l, r);
	}
}

string solve(char root) {
	int b = (1 << n);
	solve(root, 0, b - 1);
	ans[b] = 0;
	tcnt['R'] = tcnt['P'] = tcnt['S'] = 0;
	for (int i = 0; i < b; ++i) tcnt[ans[i]]++;
	if (tcnt['R'] == cnt['R'] && tcnt['S'] == cnt['S']) return string(ans);
	return "";
}

void solve() {	
	int b = (1 << n);

	string ans = "";
	string s = solve('R');
	if (s.length() != 0 && (ans.length() == 0 || ans > s)) ans = s;
	s = solve('P');
	if (s.length() != 0 && (ans.length() == 0 || ans > s)) ans = s;
	s = solve('S');
	if (s.length() != 0 && (ans.length() == 0 || ans > s)) ans = s;

	if (ans.length()) cout << ans;
	else cout << "IMPOSSIBLE";
}

int main() {
	ios_base::sync_with_stdio(0);
#ifdef FILE_IO
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";

		cin >> n >> cnt['R'] >> cnt['P'] >> cnt['S'];
		solve();

		cout << endl;
	}
}