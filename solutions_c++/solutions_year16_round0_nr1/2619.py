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

int test(int val) {
	bool v[10] = { false };

	int count = 1;
	int val2 = val;
	for (;; ++count) {
		int t = val2;
		while (t > 0) {
			v[t % 10] = true;
			t /= 10;
		}

		bool ok = true;
		FOR(i, 10) {
			if (!v[i]) { ok = false; break; }
		}
		if (ok) {
			return val2;
		}
		val2 = val * (count + 1);
	}
}

void start() {
	int n; cin >> n;
	/*	FOR(_i, n) {
			if (_i == 0)
				continue;
			cout<< _i << " " << test(_i);
		}
		*/
	FOR(_i, n) {
		int x;
		cin >> x;

		if (x == 0) {
			printf("Case #%d: INSOMNIA\n", _i + 1);
		}
		else { 
			int64 res = test(x);
			printf("Case #%d: %lld\n", _i + 1, res);
		}
	}
}

int main(void) {
	start();

	return 0;
}
