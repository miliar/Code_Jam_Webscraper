#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int,int> pii;
typedef vector<vector<int> > graph;

const double pi = acos(-1.0);

#define oned(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define twod(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

const int MAXN = 105;

int n, vf, xf, r[MAXN], x[MAXN];

void small() {
	double ans, x0 = x[0], x1 = x[1], r0 = r[0], r1 = r[1];
	
	if(n==1) {
		if(x[0]!=xf) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%.12lf\n", vf/r0);
		}
		return;
	}

	if((x[0]>xf && x[1]>xf) || (x[0]<xf && x[1]<xf)) {
		printf("IMPOSSIBLE\n");
		return;
	}
	if(x[0]==x[1]) {
		if(xf==x[0]) {
			ans = vf/(r0+r1);
		} else {
			printf("IMPOSSIBLE\n");
			return;
		}
	} else {
		double y1 = (vf*(xf-x0))/(x1-x0);
		double y0 = vf-y1;
		double t1 = y1/r1;
		double t0 = y0/r0;
		ans = max(t0, t1);
	}
	printf("%.12lf\n", ans);
}

void solve() {
	
}

int get() {
	int a, b;
	scanf("%d.%d", &a, &b);
	return a*10000+b;
}

int main() {
	freopen("B-input.in", "r", stdin);
	freopen("B-output.out", "w", stdout);
	int t; scanf("%d", &t);
	for(int c = 1; c <= t; c++) {
		scanf("%d", &n);
		vf = get();
		xf = get();
		for(int i = 0; i < n; i++) {
			r[i] = get();
			x[i] = get();
		}
		printf("Case #%d: ", c);
		small();
	}
}
