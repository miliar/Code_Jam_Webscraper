#include <iostream>
#include <fstream>

using namespace std;

int T, t;
int D;
int P[1000];

int cal(int m) {
	int r = 0;
	for (int i=0; i<D; i++) {
		if (P[i]>m) {
			r += (P[i]-1)/m;
		}
	}
	return m+r;
}

int main() {
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");
	fin >> T;
	t = T;
	while (T--) {
		fin >> D;
		for (int i=0; i<D; i++) {
			fin >> P[i];
		}
		int max = P[0];
		for (int i=1; i<D; i++) {
			if (P[i]>max)
				max = P[i];
		}
		int ans = max;
		for (int i=1; i<=max; i++) {
			if (cal(i)<ans) {
				ans = cal(i);
			}
		}
		fout << "Case #" << t-T << ": " << ans << endl;
	}
}
