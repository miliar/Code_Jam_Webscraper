#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};
int des[101][101];
int N, M;

bool rec(int x, int y, int dir){
	
	if(x<0||M<=x||y<0||N<=y)
		return true;
	else if(des[y][x]==2)
		return false;
	else
		return rec(x+dx[dir], y+dy[dir], dir);
}

int main(){

	int T, i, j;
	bool chk;
	scanf("%d", &T);
	
	for(int k=0; k<T; ++k){
		
		scanf("%d %d", &N, &M);
		
		for(i=0; i<N; ++i){
			for(j=0; j<M; ++j){
				scanf("%d", &des[i][j]);
			}
		}
		
		chk = true;
		
		for(i=0; i<N; ++i){
			for(j=0; j<M; ++j){
				
				if(des[i][j]==1){
					
					if(!( (rec(j,i,0)&&rec(j,i,1)) || (rec(j,i,2)&&rec(j,i,3)) )){
						chk = false;
						break;
					}
				}
			}
		}
		
		printf("Case #%d: ", k+1);
		
		if(chk)
			puts("YES");
		else
			puts("NO");
	}
	
	return 0;
}