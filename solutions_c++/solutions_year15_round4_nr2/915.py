#include <cstdio>
#include <cstdlib>
#include <cctype>

double r[100], c[100];
double v, g;
int n;

int main() {
	FILE *fp = fopen("B-small-attempt1.in", "r");
	FILE *fout = fopen("out.txt", "w");
	int T;
	fscanf(fp, "%d", &T);
	for (int i = 0; i < T; ++i) {
        fscanf(fp, "%d %lf %lf", &n, &v, &g);
        for (int j = 0; j < n; ++j) fscanf(fp, "%lf %lf", &r[j], &c[j]);
        fprintf(fout, "Case #%d: ", i + 1);
        if (n == 1) {
            if (c[0] == g) fprintf(fout, "%lf\n", v / r[0]);
            else fprintf(fout, "IMPOSSIBLE\n");
        }
        if (n == 2) {
            if ((c[0] > g && c[1] > g) || (c[0] < g && c[1] < g)) fprintf(fout, "IMPOSSIBLE\n");
            else if (c[0] == c[1]) {
                fprintf(fout, "%lf\n", v / (r[0] + r[1]));
            }
            else {
                double v0 =  (g - c[1]) * v / (c[0] - c[1]);
                double v1 = v - v0;
                double m = v0 / r[0];
                if (m < v1 / r[1]) m = v1 / r[1];
                fprintf(fout, "%lf\n", m);
            }
        }
	}
	fclose(fp);
	fclose(fout);
	return 0;
}