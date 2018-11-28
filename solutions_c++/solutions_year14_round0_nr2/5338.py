#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;


int main() {
	int n;
	
	FILE* fin = fopen("B-large.in", "r");
	FILE* fout = fopen("output.txt" ,"w");

	fscanf(fin, "%d", &n);

	for(int t = 1; t <= n; ++t) {
		double cost, add, target;

		fscanf(fin, "%lf%lf%lf", &cost, &add, &target);
		
		double ans = target / 2;
		double rate = 2;
		double now = 0;

		while(true) {
			now += cost / rate;
			rate += add;
			if (now + target / rate < ans) {
				ans = now + target / rate;
			} else {
				break;
			}
		}

		fprintf(fout, "Case #%d: ", t);
		fprintf(fout, "%.7f\n", ans);
	}
	fclose(fin);
	fclose(fout);
}