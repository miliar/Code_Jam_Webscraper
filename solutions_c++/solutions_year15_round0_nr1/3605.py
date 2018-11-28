#include <iostream>
#include <stdio.h>
#include <fstream>


using namespace std;

int T, N, case_number = 1;
string A;
int main() {
	ifstream ifile("a.in");
	FILE *out = fopen("a.out", "w");
	//ofstream ofile("a.out");

	ifile >> T;
	while(T-- > 0) {
		ifile >> N >> A;

		int tot = 0, sum = 0;
		for(int i = 0; i <= N; i++) {
			int d = A[i] - '0';
			tot += tot >= i ? 0 : i - tot;
			tot += d;
			sum += d;
		}

		fprintf(out, "Case #%d: %d\n", case_number++, tot - sum);
	}
}