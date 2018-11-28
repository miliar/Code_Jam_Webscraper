#include <stdio.h>
#include <math.h>

FILE *in = fopen("C-small-attempt0.in", "r");
FILE *out = fopen("C-small-attempt0.out", "w");

bool ch(int a){

	int aa[10], cc = 0;
	
	while (a != 0){
	
		cc += 1;
		aa[cc] = a%10;
		a /= 10;
	
	}

	int i;
	for (i = 1; i <= cc/2; i++){
	
		if (aa[i] != aa[cc - i + 1]) return 0;
	
	}

	return 1;
	

}
int main(){

	int test, T;

	fscanf(in, "%d", &T);
	
	for (test = 1; test <= T; test++){
	
		int a, b;

		fscanf(in, "%d %d", &a, &b);

		int i, cnt = 0;
		double aa = sqrt((double)a);
		a = sqrt((double)a);
		if (aa - (double)a > 0) a += 1;
		b = sqrt((double)b);
		for (i = a; i <= b; i++){
		
			if (ch(i) == 1){
				
				if (ch(i * i) == 1) cnt += 1;
			
			}
		
		}

		fprintf(out, "Case #%d: %d\n", test, cnt);
	
	}

	return 0;

}