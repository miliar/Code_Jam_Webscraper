#include <cstdio>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define rep(i, n) for (int i = 0, _##i = (n); i < _##i; ++i)
#define dwn(i, n) for (int i = (n); --i >= 0;)
#define repr(i, l, r) for (int i = (l), _##i = (r); i < _##i; ++i)
#define dwnr(i, l, r) for (int i = (r), _##i = (l); --i >= _##i;)
#define repi(i, a) for (__typeof((a).begin()) i = (a).begin(), _##i=(a).end(); i != _##i; ++i)
#define dwni(i, a) for (__typeof((a).rbegin()) i = (a).rbegin(), _##i=(a).rend(); i != _##i; ++i)
#define w(a) #a << ": " << (a) << "  "

char buf[101];
int lim[101];
int cur[50];
int sq[100];

void getbuf() {
	memset(buf, 0, sizeof(buf));
	cin >> buf;
	int len = strlen(buf);
	reverse(buf, buf + len);
	rep (i, 100) {
		lim[i] = max(buf[i] - '0', 0);
	}
}

bool tiebreak = false;
bool calcsq() {
	memset(sq, 0, sizeof(sq));
	rep (i, 50) {
		rep (j, 50) {
			sq[i + j] += cur[i] * cur[j];
		}
	}
	rep (i, 100) {
		if (sq[i] >= 10) return false;
	}
	return true;
}
bool ok() {
	if (calcsq() == false) return false;
	dwn (i, 100) {
		if (sq[i] < lim[i]) return true;
		if (sq[i] > lim[i]) return false;
	}
	return tiebreak;
}

int curlen = 0;
int calc(int i) {
	if (i * 2 >= curlen) {
//		cout << "fin" << endl;
//		rep (j, 50) {
//			cout << cur[j];
//		}
//		cout << endl;
//		rep (j, 100) {
//			cout << sq[j];
//		}
//		cout << endl;
//		rep (j, 100) {
//			cout << lim[j];
//		}
//		cout << endl;
		return 1;
	}
	int res = 0;
	rep (c, 4) {
		if (i == 0 && c == 0) continue;
		cur[i] = cur[curlen - i - 1] = c;
		if (!ok()) break;
		res += calc(i + 1);
	}
	cur[i] = cur[curlen - i - 1] = 0;
	return res;
}

int main() { freopen("test.in", "r", stdin); freopen("test.out", "w", stdout);
	
	int testn;
	cin >> testn;
	rep (tc, testn) {
		int curans = 0;
		tiebreak = false;
		getbuf();
		for (curlen = 1; curlen <= 50; curlen++) {
			curans -= calc(0);
		}
		tiebreak = true;
		getbuf();
		for (curlen = 1; curlen <= 50; curlen++) {
			curans += calc(0);
		}
		cout << "Case #" << tc + 1 << ": " << curans << '\n';
	}
}
