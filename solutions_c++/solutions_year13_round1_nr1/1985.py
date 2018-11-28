#include<stdio.h>
#include<stdlib.h>

FILE *in;
FILE *out;
int i, n, count[1000];
long long int a, amount, r, result;

int main(){

	in = fopen("A-small-attempt0.in", "r");
	out = fopen("A-small-attempt0.out", "w");

	fscanf(in, "%d", &n);
	for(i = 0 ; i < n ; i++){
		fscanf(in, "%lld", &a);
		fscanf(in, "%lld", &amount);
		
		r = a+1;
		while(amount>=0){
			amount -= 2*r-1;
			r = r+2;
			if(amount<0)
				break;
			count[i]++;
		}
	}
	
	for(i = 0 ; i< n ; i++)
		fprintf(out, "Case #%d: %d\n", i+1, count[i]);
	
	fclose(in);
	fclose(out);

	return 0;
}