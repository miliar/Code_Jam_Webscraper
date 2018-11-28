#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int check(char str[10001], int start, int end,char find){
	char now = str[start];
	int minus = 0;
	for (int i = start + 1; i <= end; i++){
		switch (now){
		case '1':
			now = str[i];
			break;
		case 'i':
			if (str[i] == 'i'){
				minus++;
				now = '1';
			}
			if (str[i] == 'j'){
				now = 'k';
			}
			if (str[i] == 'k'){
				minus++;
				now = 'j';
			}
			break;
		case 'j':
			if (str[i] == 'i'){
				minus++;
				now = 'k';
			}
			if (str[i] == 'j'){
				now = '1';
				minus++;
			}
			if (str[i] == 'k'){
				now = 'i';
			}
			break;
		case 'k':
			if (str[i] == 'i'){
				now = 'j';
			}
			if (str[i] == 'j'){
				now = 'i';
				minus++;
			}
			if (str[i] == 'k'){
				minus++;
				now = '1';
			}
			break;
		}
	}
	if (now == find){
		if (minus % 2 == 0)
			return 1;
		else
			return 2;
	}
	return 0;
}
int main(){

	FILE *fi = fopen("C-small-attempt4 (1).in", "r");
	FILE *fo = fopen("output.txt", "w");

	int T;

	fscanf(fi,"%d", &T);

	for (int t = 1; t <= T; t++){
		int X, L;
		int i, j;
		int pl = 0, mi = 0;
		char str[10001] = { 0, };
		char ori[10001];
		fscanf(fi,"%d %d", &X, &L);
		fscanf(fi,"%s", ori);
		for (int i = 0; i < L; i++)
			strcat(str, ori);
		int len = X*L;
		for (i = 0; i < len-2; i++){
			if (pl==0&&check(str, 0, i, 'i') == 1){
				for (j = i + 1; j < len - 1; j++){
					if (check(str, i + 1, j, 'j') == 1 && check(str, j + 1, len - 1, 'k') == 1)
					{
						fprintf(fo,"Case #%d: YES\n", t);
						i = 210000;
						j = 210000;
						break;
					}
					else if (check(str, i + 1, j, 'j') == 2 && check(str, j + 1, len - 1, 'k') == 2)
					{
						fprintf(fo,"Case #%d: YES\n", t);
						i = 210000;
						j = 210000;
						break;
					}
				}
				pl = 1;
			}
			else if (mi==0&&check(str, 0, i, 'i') == 2){
				for (j = i + 1; j < len - 1; j++){
					if (check(str, i + 1, j, 'j') == 1 && check(str, j + 1, len - 1, 'k') == 2)
					{
						fprintf(fo,"Case #%d: YES\n", t);
						i = 210000;
						j = 210000;
						break;
					}
					else if (check(str, i + 1, j, 'j') == 2 && check(str, j + 1, len - 1, 'k') == 1)
					{
						fprintf(fo,"Case #%d: YES\n", t);
						i = 210000;
						j = 210000;
						break;
					}
				}
				mi = 1;
			}
			if (mi == 1 && pl == 1)
				break;
		}
		if (i<10000)
			fprintf(fo,"Case #%d: NO\n", t);
	}
	return 0;
}