#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

char s[2010];
int a[30], b[10][30];
int ans[2000];
int ord[]={0, 2, 6, 7, 5, 4, 1, 3, 8, 9};

int main() {
	int i,j,n,kk,kj,t;

	FILE *fin, *fout;
	fin = fopen("1.in", "r");
	fout = fopen("1.txt", "w");
	for (kk=0; kk<10; kk++) {
		fscanf(fin, "%s", s);
		for (i=0; i<strlen(s); i++) b[kk][(int)(s[i] - 'A')]++;
	}
	fscanf(fin, "%d", &t);
	for (kk=0; kk<t; kk++) {
		fscanf(fin, "%s", s);
		memset(a, 0, sizeof(a));
		for (i=0; i<strlen(s); i++) a[(int)(s[i] - 'A')]++;
		n = 0;
		for (i=0; i<10; i++) {
			int now = ord[i];
			int f = 3000;
			for (j=0; j<30; j++) {
				if (b[now][j]) f = min(f, (int)(a[j]/b[now][j]));
			}
			for (j=0; j<f; j++) {
				n++; ans[n-1] = now;
			}
			for (j=0; j<30; j++) {
				if (b[now][j]) a[j] -= f*b[now][j];
			}
		}
		for (i=0; i<30; i++) if (a[i]) cout<<"FALSE";
		sort(ans, ans+n);
		fprintf(fout, "Case #%d: ",kk+1);
		for (i=0; i<n; i++) fprintf(fout, "%d", ans[i]);
		fprintf(fout, "\n"); 
	}

	fclose(fin); fclose(fout);
	return 0;
}


