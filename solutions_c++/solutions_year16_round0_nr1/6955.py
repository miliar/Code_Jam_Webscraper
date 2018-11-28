#include <cstdio>
#include <cstring>
int main() {
	FILE *fp, *fp2;
	fp = fopen("A-large.in", "r");
	fp2 = fopen("A-large.out", "w");
	int T, N, Tpie;
	fscanf(fp, "%d", &T);
	Tpie = T;
	while (Tpie--) {
		fscanf(fp, "%d", &N);
		if (N == 0) {
			fprintf(fp2, "Case #%d: INSOMNIA\n", T - Tpie);
			continue;
		}
		else {
			bool seen[10];
			int seencount = 0;
			memset(seen, false, sizeof(seen));
			long tmp = 0;
			while (seencount < 10) {
				tmp += N;
				long tmp1 = tmp;
				while (tmp1 > 0) {
					if (seen[tmp1 % 10] == false) {
						seen[tmp1 % 10] = true;
						seencount++;
					}
					tmp1 /= 10;
				}
			}
			fprintf(fp2, "Case #%d: %ld\n", T - Tpie, tmp);
		}
	}
	fclose(fp);
	fclose(fp2);
	return 0;
}