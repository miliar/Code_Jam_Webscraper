#include <iostream>
#include <fstream>

using namespace std;

void go (int t) {
	printf ("Case #%d: ", t);
	double C,F,X, R = 2.0;
	cin >> C >> F >> X;
	double best = X / R;
	double cur = 0.0;
	while (cur < best) {
		cur += C / R;
		R += F;
		best = min (best, cur + X / R);
	}
	printf ("%.7f\n", best);
}

int main () {
	int N;
	cin >> N;
	for (int i = 0; i < N; i ++) {
		go (i + 1);
	}
}
