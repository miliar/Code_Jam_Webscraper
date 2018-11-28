#include <cstdio>

int main()
{
	FILE *fp = fopen("A-large.in", "r"), *op = fopen("A-large.txt", "w");
	int t, n;
	fscanf(fp, "%d", &t);
	for (int tc = 1;tc <= t;++tc) {
		fscanf(fp, "%d", &n);
		int chk = 0, p = 0;

		while (n && chk != 1023) {
			p += n;
			for (int k = p;k;k /= 10) {
				if (!((chk >> (k % 10)) & 1))
					chk += (1 << (k % 10));
			}
		}
		fprintf(op, "Case #%d: ", tc);
		if (p) fprintf(op, "%d\n", p);
		else fprintf(op, "INSOMNIA\n");
	}

	return 0;
}