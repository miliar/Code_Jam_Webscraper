#include <stdio.h>
#include <string.h>

const int MAx = 105;
char a[MAx];

int main(){
	FILE *fi, *fo;
	fi = fopen("B-large.in", "r");
	fo = fopen("B-large.out", "w");
	int t;
	fscanf(fi,"%d", &t);
	for (int i = 1; i <= t; ++i){
		fscanf(fi,"%s", a);
		int len = strlen(a);
		
		
		int ans = 0;
		for (int i = 0; i <len-1; ++i){
			if (a[i] != a[i + 1])++ans;
		}
		if (a[len - 1] == '+')
			fprintf(fo,"Case #%d: %d\n", i, ans);
		else
			fprintf(fo,"Case #%d: %d\n", i, ans+1);
	}
	fclose(fi);
	fclose(fo);
	return 0;
}