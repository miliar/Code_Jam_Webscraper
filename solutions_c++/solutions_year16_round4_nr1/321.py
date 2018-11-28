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

char to_char[3] = {'P', 'R', 'S'};
string to_div[3] = {"PR", "RS", "SP"};

int to_num (char c) {
	return (c == 'P' ? 0 : (c == 'R' ? 1 : 2));
}

int main () {
//  ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;

	for (int ti = 0; ti < tc; ++ti) {
		int n, a[3];
		cin >> n >> a[1] >> a[0] >> a[2];

		int max_a = max(a[0], max(a[1], a[2]));
		int min_a = min(a[0], min(a[1], a[2]));

		if (max_a > min_a + 1) {
			cout << "Case #" << ti + 1 << ": IMPOSSIBLE" << endl;
		    continue;
		}

		
        for  (int i = 0; i < n; ++i) {
        	int cur_a[3];
        	int half_sum = (a[0] + a[1] + a[2]) / 2;
        	for (int i = 0; i < 3; ++i) {
				cur_a[i] = half_sum - a[(i + 2) % 3];
			}
			for (int i = 0; i < 3; ++i) {
				a[i] = cur_a[i];
			}
		}

		assert(a[0] + a[1] + a[2] == 1 && a[0] >= 0 && a[1] >= 0 && a[2] >= 0);
				int ind = -1;
		for (int i = 0; i < 3; ++i) {
			if (a[i] == 1) {
				ind = i;
			}
		}

		string s = "";
		s.pb(to_char[ind]);

		for (int i = 0, m = 1; i < n; ++i, m *= 2) {
			string next_s;
			for (int j = 0; j < m; ++j) {
				next_s.pb(to_div[to_num(s[j])][0]);
				next_s.pb(to_div[to_num(s[j])][1]);
			}
			s = next_s;
		}

		int total_n = (1 << n); 
		for (int i = 0, step = 1; i < n; ++i, step *= 2) {
			for (int j = 0; j < total_n; j += 2 * step) {
				int id = 0;
				while (id < step && s[j + id] == s[j + step + id]) {
					id++;
				}

				if (id < step && s[j + id] > s[j + step + id]) {
					for (int k = 0; k < step; ++k) {
						swap(s[j + k], s[j + step + k]);
					}
				}
			}
		}

		cout << "Case #" << ti + 1 << ": " << s << endl;
	}

	return 0;
}
