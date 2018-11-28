#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define MAX 110

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		int n, m;
		scanf("%d%d", &n, &m);
		int v[MAX][MAX];
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				scanf("%d", &v[i][j]);
		
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++){
				int cnt = 0;
				for (int k = 0; k < n; k++)
					if(v[k][j] > v[i][j]){
						cnt++;
						break;
					}
				for (int k = 0; k < m; k++)
					if(v[i][k] > v[i][j]){
						cnt++;
						break;
					}
				if(cnt == 2)
					goto fail;
			}
		printf("Case #%d: YES\n", t);
		continue;
fail:;
     		printf("Case #%d: NO\n", t);
	}
	return 0;
}
