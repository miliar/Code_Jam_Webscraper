#include <stdio.h>

FILE* input = fopen("input.txt", "r");
FILE* output = fopen("output.txt", "w");

#define MOD 1000002013

int t;

int p[10010][2] = {0,};

int main(){
	fscanf(input, "%d", &t);
	int tt;
	for(tt = 1; tt <= t; tt++){
		int n, m;
		fscanf(input, "%d%d", &n, &m);
		int i, c = 0, j, k;
		for(i = 0; i < m; i++){
			int x, y, z;
			fscanf(input, "%d%d%d", &x, &y, &z);
			for(j = 0; j < z; j++){
				p[c][0] = x;
				p[c][1] = y;
				c++;
			}
		}
		int sans = 0, eans = 0;
		for(i = 0; i < c; i++) sans += (p[i][1]-p[i][0])*(p[i][1]-p[i][0]-1)/2;
		for(i = 1; i <= 100; i++){
			for(j = 0; j < c; j++){
				if(p[j][0] > i || p[j][1] < i) continue;
				for(k = 0; k < c; k++){
					if(p[k][0] > i || p[k][1] < i) continue;
					if(p[k][0] > p[j][0] && p[k][1] > p[j][1]){
						int ttt = p[k][0];
						p[k][0] = p[j][0];
						p[j][0] = ttt;
					}
				}
			}
		}
		for(i = 0; i < c; i++) eans += (p[i][1]-p[i][0])*(p[i][1]-p[i][0]-1)/2;
		fprintf(output, "Case #%d: %d\n", tt, eans-sans);
	}
	return 0;
}