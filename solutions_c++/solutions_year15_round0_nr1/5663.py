#include<stdio.h>
char a[1001];
int main(){
	
	FILE *in, *out;
	in = fopen("A-large.in", "r");
	out = fopen("output.txt", "w");

	int t;
	fscanf(in,"%d", &t);
	for (int z = 1; z <= t; z++){
		int sm,p=0,ans=0;
		fscanf(in,"%d", &sm);
		fscanf(in,"%s", a);
		p = a[0] - 48;
		for (int i = 1; i <= sm; i++){
			if (p < i && a[i]!=48){
				ans += (i - p);
				p += (i - p);
			}
			p += a[i] - 48;
		}
		fprintf(out,"Case #%d: %d\n", z, ans);
	}

	fclose(in);
	fclose(out);

	return 0;
}