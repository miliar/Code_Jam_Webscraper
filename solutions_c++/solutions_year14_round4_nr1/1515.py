#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

ifstream inf("A-large.in");
ofstream outf("output.txt");

int a[10010];
bool u[10010];

int main() {
	int T; inf >> T;
	for (int tt = 1; tt <= T; ++tt) {
		outf << "Case #" << tt << ": ";
		int N, X; inf >> N >> X;
		for (int i = 0; i < N; i++) {
			inf >> a[i];
			u[i] = false;
		}
		sort(a, a + N);
		int ans = 0;
		int r = N - 1, i = 0;
		for (i = 0; i < N / 2 && i < r; ) {
			if (a[i] + a[r] <= X) {
				++ans;
				++i;
				--r;
			}
			else {
				++ans;
				--r;
			}
		}
		if (i == r) ++ans;
		outf << ans << "\n";
	}
}