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
int f, s;
vector<vi> fv, sv;

int main() {
	freopen("magictrick.in", "r", stdin);
	freopen("magictrick.out", "w", stdout);  
	T = ni();
	fr(test, T) {
		f = ni();
		f--;
		fv.resize(4, vector<int>(4));
		fr(i, 4)
			fr(j, 4)
				fv[i][j] = ni();
		s = ni();
		s--;
		sv.resize(4, vector<int>(4));
		fr(i, 4)
			fr(j, 4)
				sv[i][j] = ni();
		int c = 0;
		int d;
		fr(i, 4)
			fr(j, 4)
				if (fv[f][i] == sv[s][j]) {
					d = fv[f][i];
					c++;
				}
		if (c == 0)
			printf("Case #%d: Volunteer cheated!\n", test + 1);								
		else if (c == 1)
			printf("Case #%d: %d\n", test + 1, d);
		else
			printf("Case #%d: Bad magician!\n", test + 1);
	}
}
        