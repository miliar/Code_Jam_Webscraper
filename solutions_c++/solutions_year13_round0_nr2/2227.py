#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define N 104

int n, m, v[N][N];

int main(){
	int t, c = 1;
	
	scanf("%d", &t);
	while(t--){
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
				scanf("%d", &v[i][j]);
		
		int acabou = 0;
		for(int i = 0; i < n; ++i){
			for(int j = 0; j < m; ++j){
				int a = v[i][j];
				int flagh = 1, flagv = 1;
				for(int k = i-1; k >= 0; k--)
					if(v[k][j] > a) flagv = 0;
				for(int k = i+1; k < n; k++)
					if(v[k][j] > a) flagv = 0;
				for(int k = j-1; k >= 0; k--)
					if(v[i][k] > a) flagh = 0;
				for(int k = j+1; k < m; k++)
					if(v[i][k] > a) flagh = 0;
				if(flagh == 0 && flagv == 0){
					printf("Case #%d: NO\n", c++);
					acabou = 1;
					break;
				}		
			}
			if(acabou) break;
		}
		if(acabou) continue;
		printf("Case #%d: YES\n", c++);	
	}

return 0;
}
