#include <algorithm>
#include <cstring>
#include <cstdio>
using namespace std;

int main(){
	int repeat, N, M, ok, T, k;
	int P[110][110];
	scanf("%d", &repeat);
	for(int re = 1;re <= repeat;re++){
		scanf("%d %d", &N, &M);
		for(int i = 0;i < N;i++){
			for(int j = 0;j < M;j++){
				scanf("%d", &P[i][j]);
			}
		}
		ok = 1;
		for(int i = 0;i < N && ok == 1;i++){
			for(int j = 0;j < M && ok == 1;j++){
				T = P[i][j];
				
				for(k = 0;k < N;k++){
					if(P[k][j] > T) break;
				}
				if(k == N) continue;
				
				for(k = 0;k < M;k++){
					if(P[i][k] > T) break;
				}
				if(k == M) continue;

				ok = 0;
			}
		}
		printf("Case #%d: ", re);
		if(ok == 1) puts("YES");
		else puts("NO");
	}
	return 0;
}

