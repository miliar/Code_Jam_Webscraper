#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d:", casi);

		int K, C, S;
		scanf("%d%d%d", &K, &C, &S);
		if (S * C < K)
			puts(" IMPOSSIBLE");
		else{
			for (int i = 0; i <= (K - 1) / C; ++i){
				long long t = 0;
				for (int j = 0; j < C; ++j)
					t = t * K + min(i * C + j, K - 1);
				printf(" %I64d", t + 1);
			}
			puts("");
		}
	}
	return 0;
}
