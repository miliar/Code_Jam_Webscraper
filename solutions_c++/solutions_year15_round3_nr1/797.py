#include<stdio.h>
int main(){
	
	int t;
	FILE *in, *out;
	in = fopen("A-large.in", "r");
	out = fopen("output.txt", "w");

	fscanf(in,"%d", &t);
	for (int z = 0; z < t; z++){
		int r, c, w,ans;
		fscanf(in,"%d %d %d", &r, &c, &w);
		ans = (c / w)*(r-1);
		if ((c - w) % w == 0) ans += (c - w) / w + w;
		else ans += (c - w) / w + 1 + w;
		fprintf(out,"Case #%d: %d\n", z+1,ans);
	}

	fclose(in);
	fclose(out);
	return 0;
}