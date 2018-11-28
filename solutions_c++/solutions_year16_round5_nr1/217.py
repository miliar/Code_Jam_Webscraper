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

const int MAXN = 30 * 1000;

int a[MAXN];


int main () {
//  ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;

	string s;
	for (int ti = 0; ti < tc; ++ti) {
		cin >> s;
		int n = s.size();

		for (int i = 0; i < n; ++i) {
			a[i] = (s[i] == 'C' ? 0 : 1);
		}

		int res = 0;
		vector <int> cur;
		for (int i = 0; i < n; ++i) {
			if (cur.empty() || a[i] != cur.back()) {
				cur.pb(a[i]);
			} else {
				res += 10;
				cur.pop_back();
			}
		}

		res += sz(cur) / 2 * 5; 

		
		cout << "Case #" << ti + 1 << ": " << res << endl;
	}

	return 0;
}
