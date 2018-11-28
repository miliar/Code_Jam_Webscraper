#include <stdio.h>
#pragma warning(disable:4996)
int tcase, n, m,cha,su,data[11111][11111];
int map[5][5] = { { 0, 0, 0, 0, 0 }, 
				  { 0, 1, 2, 3, 4 }, 
				  { 0, 2, -1, 4, -3 },
				  { 0, 3, -4, -1, 2 }, 
				  { 0, 4, 3, -2, -1 } };
char str[11111];
FILE *in = fopen("C.in", "r");
FILE *out = fopen("C.out", "w");
int jam(int x){
	if (x < 0) return -x;
	return x;
}
int main(){
	bool sw1;
	fscanf(in,"%d", &tcase);
	for (int i1 = 1; i1 <= tcase; i1++){
		sw1 = false;
		fscanf(in,"%d %d", &n, &m);
		fscanf(in,"%s", str);
		for (int i = 0; i < n; i++){
			if (str[i] == 'i') str[i] = 2;
			else if (str[i] == 'j') str[i] = 3;
			else if (str[i] == 'k') str[i] = 4;
		}
		for (int i = 1; i<m; i++)
			for (int j = 0; j<n; j++)
				str[n*i + j] = str[j];
		n *= m;
		for (int i = 0; i<n; i++){
			su = str[i];
			data[i][i] = su;
			for (int j = i + 1; j < n; j++){
				cha = 1;
				if (su < 0) cha *= (-1);
				su = map[jam(su)][str[j]] * cha;
				data[i][j] = su;
			}
		}
		for (int i = 0; i<n; i++){
			for (int j = i + 1; j<n - 1; j++){
				if (data[0][i] == 2 && data[i + 1][j] == 3 && data[j + 1][n - 1] == 4){
					sw1 = true;
					break;
				}
			}
			if (sw1) break;
		}
		if (sw1 == true) fprintf(out,"Case #%d: YES\n", i1);
		else fprintf(out,"Case #%d: NO\n", i1);
	}
	return 0;
}