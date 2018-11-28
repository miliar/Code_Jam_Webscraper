#include <cstdio>
#include <cstring>

int arr[10], n_arr;

int main() {
	//FILE *fi = fopen("sample.in", "r");
	FILE *fi = fopen("A-large.in", "r");
	//FILE *fi = fopen("A-small-attempt0.in", "r");
	FILE *fo = fopen("output.txt", "w");

	int T, N;
	fscanf(fi, "%d", &T);
	for (int t = 1; t <= T; t++) {
		fscanf(fi, "%d", &N);
		if (N == 0) {
			fprintf(fo, "Case #%d: INSOMNIA\n", t);
			continue;
		}
		memset(arr, 0, sizeof(arr));
		n_arr = 0;
		for (int i = 1; ; i++) {
			int nN = i*N;
			while (nN) {
				if (arr[nN % 10] == 0) {
					arr[nN % 10] = 1;
					n_arr++;
				}
				nN /= 10;
			}
			if (n_arr == 10) {
				fprintf(fo, "Case #%d: %d\n", t, i*N);
				break;
			}
		}
	}
	fclose(fi);
	fclose(fo);
	return 0;
}
