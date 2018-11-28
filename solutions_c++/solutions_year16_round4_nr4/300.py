#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <bitset>
#include <sstream>
#include <queue>

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long int64;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const long long inf64 = ((long long)1 << 62) - 1;
const long double pi = acos(-1);

template <class T> T sqr (T x) {return x * x;}
template <class T> T abs (T x) {return x < 0 ? -x : x;}

const int MAXN = 5;

int n;
bool a[MAXN][MAXN];
int p[MAXN];
int res = MAXN * MAXN;
int cur = 0;

bool check() {
	for (int i = 0; i < n; ++i) {
		p[i] = i;
	}

	bool key = false;
	do {
		bool cur_key = true;
		for (int i = 0; i < n; ++i) {
			if (!a[i][p[i]]) {
				cur_key = false;
				break;
			}
		}

		key |= cur_key;

		for (int i = 0; i < n; ++i) {
			cur_key = false;
			for (int j = 0; j < n; ++j) {
				if (a[i][j] && !a[p[j]][j]) {
					cur_key = true;
					break;
				}
				if (a[i][j] && a[p[j]][j] && i == p[j]) {
					cur_key = true;
					break;
				}
		   	}
		   	if (!cur_key) {
		   		return false;
		   	}
		}

	
	} while (next_permutation(p, p + n));

	return key;

	 
}

void go(int ind1, int ind2) {
	if (ind2 == n) {
		ind1++;
		ind2 = 0;
	}

	if (ind1 == n) {
		if (check()) {
			res = min(res, cur);
		}
		return;
	}

	if (a[ind1][ind2]) {
		go(ind1, ind2 + 1);
	} else {
		cur++;
		a[ind1][ind2] = true;
		go(ind1, ind2 + 1);
		cur--;
		a[ind1][ind2] = false;
		go(ind1, ind2 + 1);
	}

}

int main () {
//  ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;

	for (int ti = 0; ti < tc; ++ti) {
		cin >> n;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				char c;
				cin >> c;
				a[i][j] = (c == '1');
			}
		}

		cur = 0;
		res = n * n;
		go(0, 0);

		cout << "Case #" << ti + 1 << ": " << res << endl;
	}

	return 0;
}
