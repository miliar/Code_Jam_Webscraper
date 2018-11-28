#include <cstdio>
#include <ctime>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
using namespace std;

#define TRACE(fmt,x) {fprintf(stderr,fmt,x);fprintf(stderr,"\n");}
#define CASE(a,b) fprintf(stderr, "%d / %d = %.2f | %.2f\n", a, b, (double)clock()/CLOCKS_PER_SEC, ((double)clock()/a*b)/CLOCKS_PER_SEC);

int N;
int m[10001];

int solve() {
	int sum = 0;
	for (int i=0; i<N-1; i++) {
		sum += max(0, m[i] - m[i+1]);
	}
	return sum;
}

int solve2() {
	int delta = 0;
	for (int i=0; i<N-1; i++)
		delta = max(delta, m[i] - m[i+1]);

	int sum = 0;
	for (int i=0; i<N-1; i++) {
		sum += min(delta, m[i]);
	}
	return sum;
}

int main() {
	int T; cin >> T;

	for (int t=1; t<=T; t++) {
		cin >> N;

		for (int i=0; i<N; i++) cin >> m[i];

		cout << "Case #" << t << ": " << solve() << " " << solve2()<< endl;

		//CASE(t,T)
	}

	return 0;
}
