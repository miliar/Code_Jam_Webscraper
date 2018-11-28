#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int qm(int now, char c);

int main(void) {
	
	int n;
	int l;
	int x;
	char arr[10010];

	FILE *fin = fopen("input.in", "r");
	FILE *fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &n);

	for(int i = 0 ; i < n ; i++) {
		int now = 1;	// 1 2 345 678
		int phase = 0;
		int possible = 0;
		fscanf(fin, "%d %d\n", &l, &x);
		fgets(arr, 10005, fin);
		for(int j = 0 ; j < x ; j++) {
			for(int k = 0 ; k < l ; k++) {
				now = qm(now, arr[k]);
				if(phase == 0 && now == 3)
					phase = 1;
				else if(phase == 1 && now == 5)
					phase = 2;
			}
		}
		if(phase == 2 && now == 2) {
			possible = 1;
		}
//////// print
		fprintf(fout, "Case #%d: ", i + 1);
		if(possible == 0) {
			fprintf(fout, "NO\n");
		}
		else {
			fprintf(fout, "YES\n");
		}
	}

	fclose(fin);
	fclose(fout);

	return 0;
}

int qm(int now, char c) {
	int n;
	if((now == 6 && c == 'i') || (now == 7 && c == 'j') || (now == 8 && c == 'k')) {
		n = 1;
	}
	else if((now == 3 && c == 'i') || (now == 4 && c == 'j') || (now == 5 && c == 'k')) {
		n = 2;
	}
	else if((now == 1 && c == 'i') || (now == 8 && c == 'j') || (now == 4 && c == 'k')) {
		n = 3;
	}
	else if((now == 5 && c == 'i') || (now == 1 && c == 'j') || (now == 6 && c == 'k')) {
		n = 4;
	}
	else if((now == 7 && c == 'i') || (now == 3 && c == 'j') || (now == 1 && c == 'k')) {
		n = 5;
	}
	else if((now == 2 && c == 'i') || (now == 5 && c == 'j') || (now == 7 && c == 'k')) {
		n = 6;
	}
	else if((now == 8 && c == 'i') || (now == 2 && c == 'j') || (now == 3 && c == 'k')) {
		n = 7;
	}
	else {
		n = 8;
	}
	return n;
}