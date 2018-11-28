#include <iostream>
#include <cstdio>
#include <fstream>

#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <string>
#include <cstring>

#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cassert>
#include <memory.h>
using namespace std;

#define fr(i, n) for (int i = 0; i < (int)(n); i++)
#define fb(i, n) for (int i = n - 1; i >= 0; i--)
#define all(a) (a).begin(), (a).end()
#define _(a, b) memset(a, b, sizeof(a))
#define mp make_pair
#define pb push_back
#define sz(v) ((int)(v).size())

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

inline int ni() { int a; scanf("%d", &a); return a; }
inline double nf() { double a; scanf("%lf", &a); return a; }
template <class T> void out(T a, T b) { bool first = true; for (T i = a; i != b; i++) { if (!first) printf(" "); first = false; cout << *i; } puts(""); }
template <class T> void outl(T a, T b) { for (T i = a; i != b; i++) cout << *i << "\n"; } 

int T;
int A, B;

bool is_fair(int x) {
	vi v;
	while (x) {
		v.pb(x % 10);
		x /= 10;
	}
	fr(i, sz(v))
		if (v[i] != v[sz(v) - i - 1])
				return false;
	return true;
}

bool is_fair_square(int x) {
	int val = (int)sqrt(1.0 * x);
	if (val * val != x)
		return false;
	return is_fair(val);
}

int solve() {
	cin >> A >> B;
	int ans = 0;
	for (int i = A; i <= B; i++) {
		if (!is_fair_square(i))
			continue;
		if (!is_fair(i))
			continue;
		ans++;
	}
	return ans;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	fr(test, T) {
		printf("Case #%d: %d\n", test + 1, solve());
	}	  
}
        