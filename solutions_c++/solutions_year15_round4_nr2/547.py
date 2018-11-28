#pragma comment(linker, "/STACK:640000000")
#include<iostream>
#include<cstdio>
#include<cassert>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<vector>
#include<bitset>
#include<algorithm>

#define pb push_back
#define ppb pop_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define ll long long
#define bit __builtin_popcountll
#define sqr(x) (x) * (x)
#define forit(it,S) for(__typeof((S).begin()) it = (S).begin(); it != (S).end(); it++)

using namespace std;

typedef pair<int, int> pii;

const double eps = 1e-9;
const double pi = acos(-1.0);

double R[111],C[111];
int r[111],c[111];

void solve() {
	int n; cin >> n;
	double V,X; cin >> V >> X;
	int v,x;
	v = int(V * 10000 + 0.5);
	x = int(X * 10000 + 0.5);
	for (int i = 0; i < n; i++) {
		cin >> R[i] >> C[i];
		r[i] = int(R[i] * 10000 + 0.5);
		c[i] = int(C[i] * 10000 + 0.5);
	}
	if (n == 1) {
		if (x == c[0]) {
			printf("%.12f\n",V / R[0]);
		} else {
			puts("IMPOSSIBLE");
		}
	} else if (n == 2) {
		if (c[0] > c[1]) {
			swap(c[0],c[1]);
			swap(r[0],r[1]);
			swap(C[0],C[1]);
			swap(R[0],R[1]);
		}
		if (c[1] < x || c[0] > x) {
			puts("IMPOSSIBLE");
		} else if (c[0] == c[1]) {
			printf("%.12f\n",V / (R[0] + R[1]));
		} else {
			double p1 = V * (X - C[0]) / (R[1] * (C[1] - C[0]));
			double p0 = (V - p1 * R[1]) / R[0];
			printf("%.12f\n",max(p0,p1));
		}
	} else {
		puts("I don't know");
	}
}

int main() {
	#ifdef LOCAL
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif

	int Cases; cin >> Cases;

	for (int Case = 1; Case <= Cases; Case++) {
		printf("Case #%d: ",Case);
		solve();
	}
	
	return 0;
}
