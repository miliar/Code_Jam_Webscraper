#include <stdio.h>
#include <algorithm>
FILE* input = fopen("input.txt", "r");
FILE* output = fopen("output.txt", "w");
int a, b;
int p[10010] = {0,};
int ans[10010][10010] = {0,};
int main(){
	int t;
	fscanf(input, "%d", &t);
	int tt;
	for(tt = 1; tt <= t; tt++){
		fprintf(output, "Case #%d: ", tt);
		fscanf(input, "%d%d", &a, &b);
		int i, j;
		for(i = 0; i < a; i++) fscanf(input, "%d", &p[i]);
		std::sort(p, p+a);
		for(j = 0; j < a; j++){
			for(i = 0; i < a; i++){
				if(j == 0) ans[i][i+j] = 1;
				else if(j == 1){
					if(p[i] + p[i+j] > b) ans[i][i+j] = 2;
					else ans[i][i+j] = 1;
				}
				else{
					if(p[i]+p[i+j] > b){
						int tmp = ans[i][i+j-1];
						if(ans[i+1][i+j] < tmp) tmp = ans[i+1][i+j];
						ans[i][i+j] = tmp + 1;
					}
					else{
						ans[i][i+j] = ans[i+1][i+j-1] + 1;
					}
				}
			}
		}
		printf("%d\n", tt);
		fprintf(output, "%d\n", ans[0][a-1]);
	}
	return 0;
}