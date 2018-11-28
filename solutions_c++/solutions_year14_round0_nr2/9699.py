#include <stdio.h>
#include <string.h>
using namespace std;

const double eps = 1e-7;
int dblcmp(double a, double b){
	if (a - b > eps) return 1;
	else if (b - a > eps) return -1;
	return 0;
}

int main(){
	FILE* fin = fopen("B-small-attempt0.in", "r");
	FILE* fout = fopen("b.out", "w");
	int T, cas, i, j, n;
	double c, f, x, k, ans, t;
	fscanf(fin, "%d", &T);
	for (cas = 1; cas <= T; cas++){
		fscanf(fin, "%lf%lf%lf", &c, &f, &x);
		ans = 0;
		k = 2;
		while(dblcmp(x / k, c / k + x / (k + f)) > 0){
			ans += c / k;
			k += f;
		}
		ans += x / k;
		fprintf(fout, "Case #%d: %.7lf\n", cas, ans);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
