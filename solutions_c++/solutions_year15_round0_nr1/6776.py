#include <stdio.h>

int main(void){
	FILE *fi=fopen("input.txt", "r"), *fo=fopen("output.txt", "w");
	int N, nn;

	fi = fopen("A-small-attempt0.in", "r");
	fscanf(fi, "%d\n", &N);

	for(nn=0; nn<N; ++nn){
		char a[1002];
		int i, n, cnt, ans=0;
		fscanf(fi, "%d %s", &n, a);
		cnt = a[0]-'0';
		for(i=1; i<=n; ++i){
			int p=a[i]-'0';
			if(cnt < i && p>0){
				ans = ans + i-cnt;
				cnt = i + p;
			}
			else{
				cnt = cnt + p;
			}
		}

		fprintf(fo, "Case #%d: %d\n", nn+1, ans);
	}

	fclose(fi);
	fclose(fo);
	return 0;
}