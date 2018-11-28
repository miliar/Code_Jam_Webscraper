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
int N, X;
vi s;
multiset<int> p;

int solve() {
	N = ni();
	X = ni();
	s.clear();
	s.resize(N);
	fr(i, N) {
		s[i] = ni();
		p.insert(s[i]);
	}
	sort(s.rbegin(), s.rend());	
	int ans = 0;	
	while (!p.empty()) {
		ans++;
		multiset<int>::iterator j = p.end();
		j--;
		int val = *j;
		p.erase(j);
		int diff = X - val;
		multiset<int>::iterator i = p.upper_bound(diff);
		if (i == p.begin())
			continue;
		i--;
		//int delta = *i;
		p.erase(i);
	}
	return ans;
}

int main() {
	freopen("datapacking.in", "r", stdin);
	freopen("datapacking.out", "w", stdout);  
	T = ni();
	fr(test, T)
		printf("Case #%d: %d\n", test + 1, solve());
}
        