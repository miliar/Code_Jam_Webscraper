#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char* argv[])
{
	FILE *file = fopen((argc > 1 ? argv[1] : "in.txt"), "r");
	FILE *g = fopen("out.txt", "w");
	int t;

	fscanf(file, "%d\n", &t);
	for (int test = 0; test < t; test++) {
		long double c, f, x;
		fscanf(file, "%lf %lf %lf\n", &c, &f, &x);
		int n = 0;
		long double t_old = x / 2.0;
		long double t_new;
		while (true) {
			t_new = t_old - x / (f*n + 2.0);
			t_new += c / (f*n + 2.0) + x / (f*(n+1) + 2.0);
			if (t_new >= t_old)
				break;
			t_old = t_new;
			n++;
		}
		fprintf(g, "Case #%d: %.7lf\n", test + 1, t_old);
	}
	fclose(file);
	fclose(g);
	return 0;
}

