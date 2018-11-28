#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <functional>
#include <cassert>
#include <map>
#include <set>
#include <list>

using namespace std;
typedef long long lli;
typedef vector<int> vi;
typedef vector<lli> vli;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef long double ld;

const int INF = 0x3f3f3f3f;
const lli LINF = 0x3f3f3f3f3f3f3f3f;

//#define _LOCAL_DEBUG_
#ifdef _LOCAL_DEBUG_
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...) 
#endif

int n, p, r, s;

map<char, char> beats;

void clear() {
}

void read() {
	scanf("%d", &n);
	scanf("%d%d%d", &r, &p, &s);
}

string find(char winner, int lvl) {
	if (lvl == 0) 
		return string(1, winner);
	char other = beats[winner];
	string left = find(other, lvl - 1);
	string right = find(winner, lvl - 1);
	if (right < left) swap(left, right);
	return left + right;
}

string solve() {
	int tr, tp, ts;
	string res = "Z";

	tr = 0, tp = 0, ts = 0;
	string rs = find('R', n);
	for (auto c : rs) tr += c == 'R', ts += c == 'S', tp += c == 'P';
	if(tr == r && tp == p && ts == s)
		res = min(res, rs);

	tr = 0, tp = 0, ts = 0;
	string ps = find('P', n);
	for (auto c : ps) tr += c == 'R', ts += c == 'S', tp += c == 'P';
	if (tr == r && tp == p && ts == s)
		res = min(res, ps);

	tr = 0, tp = 0, ts = 0;
	string ss = find('S', n);
	for (auto c : ss) tr += c == 'R', ts += c == 'S', tp += c == 'P';
	if (tr == r && tp == p && ts == s)
		res = min(res, ss);

	return res == "Z" ? "IMPOSSIBLE" : res;
}

int main() {
	beats['R'] = 'S';
	beats['S'] = 'P';
	beats['P'] = 'R';
#ifdef _LOCAL_VAN
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int it = 1; it <= t; it++) {
		clear();
		read();
		string res = solve();
		printf("Case #%d: %s\n", it, res.c_str());
	}
	return 0;
}