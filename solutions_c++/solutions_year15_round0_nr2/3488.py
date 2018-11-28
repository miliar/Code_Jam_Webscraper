#include <iostream>
#include <stdio.h>
#include <fstream>
#include <queue>
#include <algorithm>

using namespace std;

int T, N, case_number = 1, P[1000];
int main() {
	ifstream ifile("b.in");
	FILE *out = fopen("b.out", "w");

	ifile >> T;
	while(T-- > 0) {
		ifile >> N;

		for(int i = 0; i < N; i++) {
			int x;
			ifile >> P[i];
		}

		int ret = 1000;
		for(int x = 1; x <= 1000; x++) {
			int wait = 0;

			for(int i = 0; i < N; i++) {
				wait += (P[i] + x - 1) / x - 1;
			}

			ret = min(ret, x + wait);
		}

		fprintf(out, "Case #%d: %d\n", case_number++, ret);
	}
}