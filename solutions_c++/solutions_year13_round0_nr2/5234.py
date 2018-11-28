#include <stdio.h>

int g[110][110];

int main(){
	int T, m, n;
	scanf("%d", &T);
	for(int t=1;t<=T;++t){
		scanf("%d%d", &m, &n);
		for(int i=0;i<m;++i){
			for(int j=0;j<n;++j){
				scanf("%d", &g[i][j]);
			}
		}
		
		bool GJ = true;
		for(int i=0;i<m;++i){
			for(int j=0;j<n;++j){
				int h = g[i][j];
				bool ho = true;
				// check -
				for(int k=j-1;k>=0;--k){
					if(g[i][k] > h){
						ho = false;
					}
				}
				for(int k=j+1;k<n;++k){
					if(g[i][k] > h){
						ho = false;
					}
				}
				
				// check |
				bool ver = true;
				for(int k=i-1;k>=0;--k){
					if(g[k][j] > h){
						ver = false;
					}
				}
				for(int k=i+1;k<m;++k){
					if(g[k][j] > h){
						ver = false;
					}
				}
				
				if(!ho && !ver){
					GJ = false;
				}
			}
		}
		
		if(GJ) printf("Case #%d: YES\n", t);
		else   printf("Case #%d: NO\n", t);
	}
	return 0;
}
