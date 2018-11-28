#include <stdio.h>

int min(int x, int y){ return x<y? x:y; }
int max(int x, int y){ return x>y? x:y; }
int abs(int x){ return x>0? x : -x; }

int x0[1010], y0[1010], x1[1010], y1[1010];
int map[1010][1010];
int d[1010], visit[1010];

int dis(int i, int j){
	if((x1[i] >= x0[j] && x1[i] <= x1[j]) || (x0[i] >= x0[j] && x0[i] <= x1[j]) ||
		(x1[j] >= x0[i] && x1[j] <= x1[i]) || (x0[j] >= x0[i] && x0[j] <= x1[i])){
		if(y1[i] < y0[j]) return y0[j] - y1[i] - 1;
		else return y0[i] - y1[j] - 1;
	}
	if((y1[i] >= y0[j] && y1[i] <= y1[j]) || (y0[i] >= y0[j] && y0[i] <= y1[j]) ||
		(y1[j] >= y0[i] && y1[j] <= y1[i]) || (y0[j] >= y0[i] && y0[j] <= y1[i])){
		if(x1[i] < x0[j]) return x0[j] - x1[i] - 1;
		else return x0[i] - x1[j] - 1;
	}
	return max(min(abs(y0[j]-y1[i]), abs(y0[i]-y1[j])), min(abs(x0[j]-x1[i]), abs(x0[i]-x1[j]))) - 1;
}

int main(){
	int T, w, h, b;
	scanf("%d", &T);
	for(int t=1; t<=T; ++t){
		scanf("%d%d%d", &w, &h, &b);
		for(int i=0; i<b; ++i){
			scanf("%d%d%d%d", &x0[i], &y0[i], &x1[i], &y1[i]);
		}
		x0[b]   = -1; y0[b]   = 0; x1[b]   = -1; y1[b]   = h-1;
		x0[b+1] = w;  y0[b+1] = 0; x1[b+1] =  w; y1[b+1] = h-1;
		b+=2;
		for(int i=0; i<b; ++i){
			map[i][i] = 0;
			for(int j=i+1; j<b; ++j){
				map[i][j] = map[j][i] = dis(i, j);
			}
		}
		/*
		for(int i=0; i<b; ++i){
			for(int j=0; j<b; ++j) printf("%d ", map[i][j]);
			printf("\n");
		}*/
		d[b-1] = 0;
		for(int i=0; i<b-1; ++i) d[i] = 1000000;
		for(int i=0; i<b; ++i) visit[i] = false;
		for(int i=0; i<b; ++i){
			int min = 1000000, pos;
			for(int j=0; j<b; ++j){
				if(!visit[j]  && d[j] < min){
					min = d[j];
					pos = j;
				}
			}
			visit[pos] = true;
			for(int j=0; j<b; ++j){
				if(d[pos] + map[pos][j] < d[j]) d[j] = d[pos] + map[pos][j];
			}
		}
		//for(int i=0; i<b; ++i) printf("%d ", d[i]);
		//printf("\n");
		printf("Case #%d: %d\n", t, d[b-2]);
	}
	
	return 0;
}
