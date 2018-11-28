#include <stdio.h>
FILE* input = fopen("input.txt", "r");
FILE* output = fopen("output.txt", "w");
int t;
int a;
int ansch = 0;
int p[30] = {0,};
int q[30] = {0,};
int r[30] = {0,};
//int s[30] = {0,};
//int u[30] = {0,};
void play(int x){
	int i, j;
	if(x > a){
		ansch = 1;
		return ;
	}
	for(i = 0; i < a; i++){
		if(r[i] != 0) continue;
		int ch = 0;
				int m = 0;
				for(j = 0; j < i; j++){
					if(r[j] != 0 && p[j] > m) m = p[j];
				}
				if(m != p[i]-1) ch = 1;
				m = 0;
				for(j = i+1; j < a; j++){
					if(r[j] != 0 && q[j] > m) m = q[j];
				}
				if(m != q[i]-1) ch = 1;
				if(ch == 0){
					r[i] = x;
					play(x+1);
					if(ansch == 1) return ;
					r[i] = 0;
				}
			}
}
int main(){
	fscanf(input, "%d", &t);
	int tt;
	for(tt = 1; tt <= t; tt++){
		ansch = 0;
		fscanf(input, "%d", &a);
		int i, j;
		for(i = 0; i < a; i++) fscanf(input, "%d", &p[i]);
		for(i = 0; i < a; i++) fscanf(input, "%d", &q[i]);
		int c;
		play(1);
		fprintf(output, "Case #%d: ", tt);
		for(i = 0; i < a; i++) fprintf(output, "%d ", r[i]);
		fprintf(output, "\n");
/*		for(i = 0; i < a; i++){
			int m = 0;
			for(j = 0; j < i; j++){
				if(r[j] < r[i] && s[j] > m) m = s[j];
			}
			s[i] = m+1;
		}
		for(i = a-1; i >= 0; i--){
			int m = 0;
			for(j = a-1; j > i; j--){
				if(r[j] < r[i] && u[j] > m) m = u[j];
			}
			u[i] = m+1;
		}
		for(i = 0; i < a; i++) fprintf(output, "%d ", s[i]);
		fprintf(output, "\n");
		for(i = 0; i < a; i++) fprintf(output, "%d ", u[i]);
		fprintf(output, "\n");*/
		for(i = 0; i < a; i++) r[i] = 0;
	}
	return 0;
}