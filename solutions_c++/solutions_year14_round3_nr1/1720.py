#include<stdio.h>
#include<stdlib.h>
#include<math.h>

long int binarycheck(long int n){
	long int tmp;
	for (long int i = 1;; i++){
		tmp = (long int)pow(2.0, i);
		if (tmp == n)return i;
		else if (tmp > n)return 0;
	}
}

long int gcd(long int x,long int y){
	if (y == 0)return x;
	else return gcd(y, x%y);
}

void func(int cnum,FILE *fi,FILE *fo){
	long int P, Q,Gcd;
	int possible;
	fscanf(fi,"%ld/%ld", &P, &Q);

	Gcd = gcd(P, Q);
	P /= Gcd;
	Q /= Gcd;

	if (binarycheck(Q)){
		possible = binarycheck(Q);
		int j;
		for (j = 1; j <= possible; j++){
			P *= 2;
			if (P>=Q)break;
		}
		fprintf(fo, "Case #%d: %ld\n", cnum, j);
	}
	else{
		fprintf(fo, "Case #%d: impossible\n", cnum);
	}
}

int main(void){
	FILE *fi = fopen("A-small-attempt0.in", "r");
	FILE *fo = fopen("testOutput.txt", "w");
	int T;
	fscanf(fi,"%d", &T);
	for (int i = 1; i <= T; i++){
		func(i,fi,fo);
	}
}