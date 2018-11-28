#include <cstdio>
#include <list>

using namespace std;

int main() {
	FILE * fin = fopen("B.in", "r"), * fout = fopen("B.out", "w");
	int t, T, i, N, ans, b, bi;
	list<int> A;
	list<int>::iterator it, bit;
	fscanf(fin, "%d", &T);
	for (t = 1; t <= T; ++t) {
		ans = 0;
		A.clear();
		fscanf(fin, "%d", &N);
		for (i = 0; i < N; ++i) {
			fscanf(fin, "%d", &b);
			A.push_back(b);
		}
		while (!A.empty()) {
			i = 0;
			b = 1000000001;
			bi = 0;
			for (it = A.begin(); it != A.end(); ++it) {
				if (*it <= b) {
					b = *it;
					bit = it;
					bi = i;
				}
				++i;
			}
			if (bi < A.size() - bi - 1) {
				ans += bi;
			} else {
				ans += A.size() - bi - 1;
			}
			A.erase(bit);
		}
		fprintf(fout, "Case #%d: %d\n", t, ans);
	}
	return 0;
}