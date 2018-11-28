#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAXN (1 << 10)
#define EPS (1e-10)
using namespace std;

int n;
int used[MAXN];
double a[MAXN];
double b[MAXN];

int playDeceitfulTurn(double val) {
	int candidate = -1;
	for (int i=0; i < n; ++i) if (!used[i]) {
		if (val > b[i]) continue;
		candidate = i;
	}

	// smallest unmarked to score a point
	for (int i=0; i < n; ++i) if (!used[i]) {
		if (b[i] < val) {
			used[i] = true;
			return i;
		} else break;
	}

	if (candidate != -1) {
		used[candidate] = true;
		return candidate;
	}

	// no bigger value => return smallest unmarked
	for (int i=0; i < n; ++i) if (!used[i]) {
		used[i] = true;
		return i;
	}
}

int playTurn(double val) {
	for (int i=0; i < n; ++i) if (!used[i]) {
		if (val > b[i]) continue;
		used[i] = true;
		return i;
	}
	// no bigger value => return smallest unmarked
	for (int i=0; i < n; ++i) if (!used[i]) {
		used[i] = true;
		return i;
	}
}

inline void solveWar() {
	memset(used, 0, sizeof used);
	sort(a, a+n);
	sort(b, b+n);

	int score = 0;
	for (int i=0; i < n; ++i) {
		double cura = a[i];
		double curb = b[ playTurn(cura) ];
		//printf("Chosen: %lf and %lf\n", cura, curb);
		if (cura > curb) {
			score ++;
		}
	}

	printf("%d\n", score);
}

inline void solveDeceitfulWar() {
	memset(used, 0, sizeof used);
	sort(a, a+n);
	sort(b, b+n);

	int score = 0;
	for (int i=0; i < n; ++i) {
		double cura = a[i];
		double curb = b[ playDeceitfulTurn(cura) ];
	//	printf("Chosen: %lf and %lf\n", cura, curb);
		if (cura > curb) {
			score ++;
		}
	}

	printf("%d ", score);
}

inline void read() {
	scanf("%d", &n);
	for (int i=0; i < n; ++i) scanf("%lf", &a[i]);
	for (int i=0; i < n; ++i) scanf("%lf", &b[i]);
}

int main() {
	int brt;
	scanf("%d", &brt);

	for (int test=0; test < brt; ++test) {
		printf("Case #%d: ", test+1);
		read();
		solveDeceitfulWar();
		solveWar();
	}
	return 0;
}