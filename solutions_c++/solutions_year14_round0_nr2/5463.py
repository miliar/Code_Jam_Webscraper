#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

#define forn(a,n) for(int a = 0; a<(n); ++a)

double c, f, x;
int T;
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	//freopen("B-small.in", "r", stdin);

	cin >> T;
	forn(t,T) {
		cin >> c >> f >> x;

		double best = x/2, ratio = 2.0, acum = 0.0;

		while(acum < best) {
			acum += c/ratio;
			ratio += f;

			best = min(best, acum + x/ratio);
		}

		printf("Case #%i: %.7f\n", t+1, best);
	}
}