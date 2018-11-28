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
double C, F, X;

double solve() {
	C = nf();
	F = nf();
	X = nf();
	double add = 2;
	double ans = 0;
	double work = C / F;

	while (true) {
		double next_farm = C / add;
		double till_end = X / add;
		if (next_farm < till_end) {			
			ans += next_farm;
			double nt = (X - C) / add;
			if (work < nt) {
				add += F;
			} else {
				ans += nt;
				break;
			}
		} else {
			ans += till_end;
			break;
		}
	}

	return ans;
}

int main() {
	freopen("cookieclicker.in", "r", stdin);
	freopen("cookieclicker.out", "w", stdout);
	T = ni();
	fr(test, T) {
		printf("Case #%d: %.7lf\n", test + 1, solve());
	}
}
        