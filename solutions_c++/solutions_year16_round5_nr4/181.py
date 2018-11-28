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

const int MAXN = 120;

int good[MAXN][MAXN];
int bad[MAXN];

int read() {
	char c;
	cin >> c;
	return (c - '0');
}

int main () {
//  ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;

	for (int ti = 0; ti < tc; ++ti) {
		int n, len;
        cin >> n >> len;

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < len; ++j) {
				good[i][j] = read();
			}
		}

		for (int i = 0; i < len; ++i) {
			bad[i] = read();
		}

		bool key = true;
		for (int i = 0; i < n; ++i) {
			bool key0 = true;
			for (int j = 0; j < len; ++j) {
				if (good[i][j] != bad[j]) {
					key0 = false;
					break;
				}
			}
			if (key0) {
				key = false;
				break;
			}
		}

		if (!key) {
			cout << "Case #" << ti + 1 << ": IMPOSSIBLE" << endl;
	    	continue;	
		}
		
		string res0 = "", res1 = "";
		for (int i = 0; i < len; ++i) {
			res0.pb('0');
			res1.pb('?');
			if (i < len - 1) {
				res0.pb('1');
				res1.pb('0');
			}
		}

        cout << "Case #" << ti + 1 << ": " << res0 << " " << res1 << endl;
    }

	return 0;
}
