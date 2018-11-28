#include<stdio.h>

void func(FILE *fi, FILE *fo, int k){
	int r, c, w;
	fscanf(fi,"%d %d %d", &r, &c, &w);

	if (c%w == 0){
		fprintf(fo,"Case #%d: %d\n",k , c / w * r + w -1);
	}
	else{
		fprintf(fo, "Case #%d: %d\n",k , c / w * r + w);
	}
}

int main(void){
	FILE *fi, *fo;
	fi = fopen("A-large.in", "r");
	fo = fopen("A-large.out", "w");

	int T;
	fscanf(fi, "%d", &T);

	for (int i = 0; i < T; i++){
		func(fi, fo, i+1);
	}
}