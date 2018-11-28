#include <stdio.h>

FILE * pw;
FILE * pr;

int main(){
	pw = fopen("out.txt", "w");
	pr = fopen("in.txt", "r");
	
	int i, j, k, n, m;
	int c, r;
	int a[4];
	int f, t;
	
	fscanf(pr, "%d", &n);
	for(m = 1; m <= n; m++){
		fprintf(pw, "Case #%d: ", m);
		c = 0;
		
		fscanf(pr, "%d", &r);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++){
				fscanf(pr, "%d", &t);
				if(i+1 == r)
					a[j] = t;
			}
			
		fscanf(pr, "%d", &r);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++){
				fscanf(pr, "%d", &t);
				if(i+1 == r){
					for(k = 0; k < 4;k++){
						if(t == a[k]){
							++c;
							f = t;
						}
					}
				}
			}
			
		if(c == 0) fprintf(pw, "Volunteer cheated!\n");
		else if(c > 1) fprintf(pw, "Bad magician!\n");
		else fprintf(pw, "%d\n", f);
	}
	return 0;
}
