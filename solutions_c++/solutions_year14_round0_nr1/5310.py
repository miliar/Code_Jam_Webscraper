#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;


int main() {
	int n;
	
	FILE* fin = fopen("A-small-attempt0.in", "r");
	FILE* fout = fopen("output.txt" ,"w");

	fscanf(fin, "%d", &n);

	for(int k = 1; k <= n; ++k) {
		int a, b;
		int aa[4][4];
		int bb[4][4];

		fscanf(fin, "%d", &a);
		a--;
		for(int i = 0; i < 4; ++i) {
			for(int j = 0; j < 4; ++j) {
				fscanf(fin, "%d", &aa[i][j]);
			}
		}


		fscanf(fin, "%d", &b);
		b--;

		for(int i = 0; i < 4; ++i) {
			for(int j = 0; j < 4; ++j) {
				fscanf(fin, "%d", &bb[i][j]);
			}
		}

		int buf[32];
		memset(buf, 0, sizeof(buf));
		
		for(int i = 0; i < 4; ++i) {
			buf[aa[a][i]] ++;
			buf[bb[b][i]] ++;
		}

		int ans = 0;
		int cnt = 0;
		for(int i = 1; i<=16; ++i) {
			if (buf[i] == 2) {
				cnt ++;
				ans = i;
			}
		}

		fprintf(fout, "Case #%d: ", k);
		if (cnt == 0) {
			fprintf(fout, "Volunteer cheated!\n");
		} else if (cnt == 1) {
			fprintf(fout, "%d\n", ans);
		} else {
			fprintf(fout, "Bad magician!\n");
		}
	}
	fclose(fin);
	fclose(fout);
}