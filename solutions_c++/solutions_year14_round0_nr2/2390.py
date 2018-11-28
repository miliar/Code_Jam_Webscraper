#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

#define IN_FILE "B-large.in"
#define OUT_FILE "output.txt"

using namespace std;

int main(int argc, char const *argv[]) { 

	freopen(IN_FILE, "r", stdin);
	freopen(OUT_FILE, "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {

		double C, F, X;
		cin >> C >> F >> X;

		int farms = 0;
		double current = X / 2, prev = 0;

		do {
			prev = current;
			current = 0;
			++farms;

			for (int k = 0; k < farms; ++k) {
				current += 1.0 / (2 + k*F);
			}

			current *= C;
			current += X / (farms*F + 2);

		} while (current < prev);

		printf("Case #%d: %.7f\n", t + 1, prev);

	}

	return 0;
}