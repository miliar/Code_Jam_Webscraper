#include <stdio.h>
#include <stdlib.h>

int twotwo(long long int num){
	while (1){
		if (num == 1)
			return 1;
		if (num % 2 == 1)
			return 0;
		num /= 2;
	}
}
int main(){
	int N;
	long long int p, q;
	FILE *fi = fopen("A-small-attempt1.in", "r");
	FILE *fo = fopen("output.txt", "w");
	fscanf(fi,"%d", &N);

	for(int i=1;i<=N;i++){
		fscanf(fi,"%lld/%lld", &p, &q);
		int anc = 0;
		double pq;
		pq = (double)p / q;
		if (twotwo(q)==0)
			fprintf(fo,"Case #%d: impossible\n", i);
		else{
			while (pq < 1){
				pq *= 2;
				anc++;
			}

			fprintf(fo,"Case #%d: %d\n", i, anc);
		}
	}

	return 0;
}