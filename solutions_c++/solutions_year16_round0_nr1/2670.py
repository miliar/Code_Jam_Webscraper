#include <iostream>
using namespace std;

int main() {
	int i,k,x,T;
	int a[10];

	FILE *fin, *fout;
	fin = fopen("1.in", "r");
	fout = fopen("1.txt", "w");
	fscanf(fin, "%d", &T);
	for (k=0; k<T; k++) {
		fscanf(fin, "%d", &x);
		fprintf(fout, "Case #%d: ",k+1);
		if (!x) {
			fprintf(fout, "INSOMNIA\n");
			continue;
		}
		for (i=0; i<10; i++) a[i] = 0;
		i = 1; int sum = 0;
		while (true) {
			int now = i*x; 
			int pre = now;
			while (now > 0) {
				if (!a[now%10]) {
					sum++; a[now%10] = 1;
				}
				now /= 10;
			}
			if (sum==10) {
				fprintf(fout, "%d\n", pre); break;
			} //else fprintf(fout, "%d-%d ",pre,sum);
			i++;
		}
	}

	fclose(fin); fclose(fout);
	return 0;
}


