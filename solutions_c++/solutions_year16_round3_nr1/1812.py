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


void start() {
	int n; cin >> n;
	FOR(_i, n) {
		int x;
		cin >> x;


		string res;
		vi p(x);
		int sum = 0;
		FOR(i, x) {
			cin >> p[i];
			sum += p[i];
		}

		while (sum > 2) {
			if (res.size() != 0) {
				res += ' ';
			}

			int maxi = p[0];
			FOR2(i, 1, x) {
				if (p[i] > maxi) {
					maxi = p[i];
				}
			}

			int count = 0;
			FOR(i, x) {
				if (p[i] == maxi) {
					res += 'A' + i;
					p[i] --;
					sum--;
					if (++count == 2 || sum == 2) break;
				}
			}
		}

		if (sum > 0) {
			if (res.size() != 0) {
				res += ' ';
			}

			FOR(i, x) {
				if (p[i] != 0) {
					res += 'A' + i; p[i]--;
				}
			}
			FOR(i, x) {
				if (p[i] != 0) res += 'A' + i;
			}
		}

		printf("Case #%d: %s\n", _i + 1, res.c_str());
	}
}

int main(void) {
	start();

	return 0;
}
