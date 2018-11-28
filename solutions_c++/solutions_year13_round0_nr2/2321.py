#include <stdio.h>
#include <string.h>
#include <set>
int target[101][101];
int N, M;
bool isFeasible(void){
	for(int r=0;r<N;++r){
		for(int c=0;c<M;++c){
			bool ok=true;
			for(int i=0;i<N;++i){
				if(target[i][c]>target[r][c]){
					ok=false;
					break;
				}
			}
			if(ok){
				continue;
			}
			ok=true;
			for(int j=0;j<M;++j){
				if(target[r][j]>target[r][c]){
					ok=false;
					break;
				}
			}
			if(!ok){
				return false;
			}
		}
	}
	return true;
}

int main(int argc, char *argv){
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;++c){
		scanf("%d%d", &N, &M);
		for(int i=0;i<N;++i){
			for(int j=0;j<M;++j){
				scanf("%d", &target[i][j]);
			}
		}
		bool feasible=isFeasible();
		printf("Case #%d: %s\n", c, feasible?"YES":"NO");
	}


}

