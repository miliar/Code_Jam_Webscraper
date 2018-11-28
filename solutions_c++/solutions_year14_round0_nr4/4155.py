#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	FILE * fin = fopen("D.in", "r"), * fout = fopen("D.out", "w");
	int T, t, N, i, j, k;
	vector<double> naomi, ken;
	fscanf(fin, "%d", &T);
	for (t = 1; t <= T; ++t) {
		fscanf(fin, "%d", &N);
		naomi.resize(N);
		ken.resize(N);
		for (i = 0; i < N; ++i) {
			fscanf(fin, "%lf", &naomi[i]);
		}
		for (i = 0; i < N; ++i) {
			fscanf(fin, "%lf", &ken[i]);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		j = 0;
		for (i = 0; i < N; ++i) {
			if (naomi[i] > ken[j]) {
				++j;
			}
		}
		k = 0;
		for (i = 0; i < N; ++i) {
			if (ken[i] > naomi[k]) {
				++k;
			}
		}
		fprintf(fout, "Case #%d: %d %d\n", t, j, N - k);
	}
	return 0;
}
