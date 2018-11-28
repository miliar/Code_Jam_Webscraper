#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int main() {
	ifstream inf("D-large.in");
	ofstream outf("output.txt");

	int T; inf >> T;
	for (int tc = 1; tc <= T; tc++) {
		outf << "Case #" << tc << ": ";
		int N; inf >> N;
		set<double> w[2];
		for (int k = 0; k < 2; k++) {
			for (int i = 0; i < N; i++) {
				double a; inf >> a;
				w[k].insert(a);
			}
		}
		set<double> cw[2] = { w[0], w[1] };
		int ans[2] = { 0, 0 };
		for (int i = 0; i < N; i++) {
			if (*--w[0].end() < *--w[1].end()) {
				w[0].erase(w[0].begin());
				w[1].erase(--w[1].end());
			}
			else {
				//if (*w[0].begin() > *w[1].begin()) ++ans[0];
				w[0].erase(--w[0].end());
				w[1].erase(--w[1].end());
				++ans[0];
			}
			auto it = cw[1].upper_bound(*cw[0].begin());
			if (it == cw[1].end()) {
				++ans[1];
				cw[1].erase(cw[1].begin());
			}
			else {
				cw[1].erase(it);
			}
			cw[0].erase(cw[0].begin());
		}
		outf << ans[0] << ' ' << ans[1] << '\n';
	}
}