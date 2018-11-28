#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

#define MAXN 128
#define EPS 1E-13

typedef long double tint;

int N;
tint V, X;

struct source {
	tint r, t;
} n[MAXN];

bool operator<(const source &s1, const source &s2) {
	if (s1.t != s2.t) return s1.t < s2.t;
	else return s1.r < s2.r;
}

bool possible(double T) {
	tint xv, v;
	
	xv = v = 0.0;
	for (int i=0; i<N; i++) {
		if (v + T*n[i].r < V) {
			xv += T*n[i].r*n[i].t;
			v += T*n[i].r;
		} else {
			xv += (V-v)*n[i].t;
			v += V-v;
			break;
		}
	}
	if (v < V-EPS || xv > X*V) return false;
	
	xv = v = 0.0;
	for (int i=N-1; i>=0; i--) {
		if (v + T*n[i].r < V) {
			xv += T*n[i].r*n[i].t;
			v += T*n[i].r;
		} else {
			xv += (V-v)*n[i].t;
			v += V-v;
			break;
		}
	}
	if (v < V-EPS || xv < X*V) return false;
	
	return true;
}

int main() {
	int T, t, i;
	tint S, E, M;
	
	cin >> T;
	for (t=1; t<=T; t++) {
		cin >> N >> V >> X;
		
		S = E = 0.0;
		for (i=0; i<N; i++) {
			cin >> n[i].r >> n[i].t;
			E = max(E, V/n[i].r+EPS);
		}
		sort(n, n+N);
		
		cout << "Case #" << t << ": ";
		if (!possible(E)) cout << "IMPOSSIBLE" << endl;
		else {
			while (E-S > EPS) {
				M = (S+E)/2.0;
				if (possible(M)) E = M;
				else S = M;
			}
			printf("%.16lf\n", (double)(S+E)/2.0);
		}
	}

	return 0;
}
