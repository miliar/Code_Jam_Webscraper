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

const int MAXN = 300;

ldb p[MAXN];
ldb lpol[MAXN][MAXN], rpol[MAXN][MAXN];

void mult_pol(ldb pol[MAXN], ldb a, ldb b, ldb res[MAXN]) {
	res[0] = b * pol[0];
	for (int i = 1; i < MAXN; ++i) {
		res[i] = a * pol[i - 1] + b * pol[i];
	}
} 

int main () {
//  ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;

	for (int ti = 0; ti < tc; ++ti) {
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; ++i) {
			cin >> p[i];
		}
		sort(p, p + n);

		for (int i = 0; i <= n; ++i) {
			for (int j = 0; j <= n; ++j) {
				lpol[i][j] = 0;
				rpol[i][j] = 0;
			}
		}
	   	
	   	lpol[0][0] = 1.0;
	   	rpol[0][0] = 1.0;
	   	for (int i = 1; i <= n; ++i) {
	   		mult_pol(lpol[i - 1], p[i - 1], 1 - p[i - 1], lpol[i]);
	   		mult_pol(rpol[i - 1], p[n - i], 1 - p[n - i], rpol[i]);		
	   	}

	   	ldb res = 0;
	   	for (int i = 0; i <= k; ++i) {
	   		ldb cur_res = 0;
	   		for (int j = 0; j <= k / 2; ++j) {
	   			cur_res += lpol[i][j] * rpol[k - i][k / 2 - j];
	   		}
	   		res = max(cur_res, res);
	   	}

	   	cout.precision(20);
		cout << "Case #" << ti + 1 << ": " << res << endl;
	}

	return 0;
}
