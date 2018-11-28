#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define maxn  1000000
using namespace std;
bool a[10];
long long int ans[maxn];
int main(){
	FILE *in, *out;
	in = fopen("in.txt", "r");
	out = fopen("output.txt", "w");
	int t, n;
	for (int i = 1; i <= maxn; i++) {
		bool f = false;
		int j;
		for (j = 0; j < 10; j++)
			a[j] = false;
		for (j = 1; !f; j++) {
			int y = i*j;
			while (y > 0) {
				a[y % 10] = true;
				y /= 10;
			}
			f = true;
			for (int k = 0; k < 10; k++)
				f &= a[k];
		}
		ans[i] = i*(j-1);
	}
	
	fscanf(in,"%d", &t);
	for (int i = 1; i <= t; i++) {
		int x;
		fscanf(in, "%d", &x);
		if (x == 0)
			fprintf(out, "Case #%d: INSOMNIA \n",i);
		else
			fprintf(out, "Case #%d: %d\n",i, ans[x]);
	}
	fclose(in);
	fclose(out);
	return 0;
}