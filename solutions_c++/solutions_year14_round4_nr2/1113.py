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

inline int get_bit(int x, int k) {
	return (x >> k) & 1;
}

int T;
int N;
vi a;

int solve() {
	N = ni();
	a.clear();
	a.resize(N);
	int mx = -1, p = 0;
	fr(i, N) {
		a[i] = ni();
		if (a[i] > mx) {
			mx = a[i], p = i;
		}
	}

	int best = 2000000000;
	int maxmask = 1 << N;
	fr(mask, maxmask) {
		if (get_bit(mask, p))
			continue;
		set<int> l, r;
		int lr = 0, rl = 0;
		fr(i, N)
			if (get_bit(mask, i)) {
				r.insert(i);
				if (i < p)
					lr++;
			} else {
				l.insert(i);					
				if (i > p)
					rl++;
			}
		//int cur = lr * rl + (lr + rl);
		int cur = 0;
		vi curl, curr;
		fr(i, N) {
			if (l.count(i))
				curl.pb(a[i]);
			else
				curr.pb(a[i]);
		}
		for(set<int>::iterator i = l.begin(); i != l.end(); i++)
			for (set<int>::iterator j = r.begin(); j != r.end(); j++)
				if (*i > *j)
					cur++;
		for (int i = 0; i < sz(curl); i++) {
			for (int j = 0; j < sz(curl) - 1; j++) {
				if (curl[j] > curl[j + 1]) {
					swap(curl[j], curl[j + 1]);
					cur++;
				}
			}
		}
		for (int i = 0; i < sz(curr); i++) {
			for (int j = 0; j < sz(curr) - 1; j++) {
				if (curr[j] < curr[j + 1]) {
					swap(curr[j], curr[j + 1]);
					cur++;
				}
			}
		}
		best = min(best, cur);		
	}
	return best;
}

int main() {
	freopen("upanddown.in", "r", stdin);
	freopen("upanddown.out", "w", stdout);
	T = ni();
	fr(test, T)
		printf("Case #%d: %d\n", test + 1, solve());	  
}
        