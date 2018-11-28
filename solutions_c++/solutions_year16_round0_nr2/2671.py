#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pI;
typedef pair<string, int> pSI;
typedef pair<int, string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second




void flip(string &v, int len) {
	REVFOR(i, len) {
		v[i] = v[i] == '+' ? '-' : '+';
	}

	reverse(v.begin(), v.begin() + len);
}

void flip(string &v) {
	flip(v, v.size());
}

int test(string &v) {
	if (v.size() == 0)
		return 0;

	if (v[v.size() - 1] == '+')
		return test(v.substr(0, v.size() - 1));

	if (v[0] == '-') {
		flip(v);
		return 1 + test(v);
	}
	else {
		int j = 1;
		while (j < v.size() && v[j] == '+') {
			++j;
		}
		flip(v, j);
		return 1 + test(v);
	}
}

void start() {
	int n; cin >> n;
	FOR(_i, n) {
		string x; cin >> x;

		int64 res = test(x);
		printf("Case #%d: %lld\n", _i + 1, res);
	}
}

int main(void) {
	start();

	return 0;
}
