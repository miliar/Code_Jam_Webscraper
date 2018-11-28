#include <algorithm>
#include <iostream>
#include <cassert>
#include <cstdio>
#include <cstring>

using namespace std;

char grid[110][110];

int M,N;

int rct[110];
int cct[110];

int main(){

	int i,j,ct,t1;

	int t;

	scanf("%d",&t);

	for(t1 = 1; t1 <= t; ++t1){
		scanf("%d%d",&M,&N);

		memset(rct,0,sizeof(rct));
		memset(cct,0,sizeof(cct));
		ct = 0;
		for(i = 0; i < M; ++i) scanf("%s",grid[i]);
		for(i = 0; i < M; ++i){
			for(j = 0; j < N; ++j){
				if(grid[i][j]^'.'){
					ct += grid[i][j] == '<';
					break;
				}
			}

			for(j = N-1; j >= 0; --j){
				if(grid[i][j]^'.'){
					ct += grid[i][j] == '>';
					break;
				}
			}
		}

		for(j = 0; j < N; ++j){
			for(i = 0; i < M; ++i){
				if(grid[i][j]^'.'){
					ct += grid[i][j] == '^';
					break;
				}
			}

			for(i = M-1; i >= 0; --i){
				if(grid[i][j]^'.'){
					ct += grid[i][j] == 'v';
					break;
				}
			}
		}

		for(i  =0; i < M; ++i){
			for(j = 0; j < N; ++j){
				if(grid[i][j]^'.') ++rct[i], ++cct[j];
			}
		}

		for(i  =0; i < M; ++i){
			for(j = 0; j < N; ++j){
				if(grid[i][j] == '.') continue;
				if(rct[i] == 1 && cct[j] == 1) break;
			}
			if(j < N) break;
		}

		if(i < M) printf("Case #%d: IMPOSSIBLE\n",t1);
		else printf("Case #%d: %d\n",t1,ct);
	}


	return 0;
}
