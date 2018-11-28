#include <stdio.h>

int Map[102][102];
int a[102],b[102];

int main(){
	int T,n,m;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas ++){
		scanf("%d %d",&n,&m);
		for(int i = 0; i < n; i ++){

			for(int j = 0; j < m; j ++){
				scanf("%d",&Map[i][j]);
				if(j == 0){a[i] = Map[i][j];}
				if(Map[i][j] > a[i]) a[i] = Map[i][j];
				if(i == 0){b[j] = Map[i][j];}
				if(Map[i][j] > b[j]) b[j] = Map[i][j];
			}

		}
		int ans = 1;
		for(int i = 0; i < n; i ++){
			for(int j = 0; j < m;j ++){
				if(Map[i][j] < a[i] && Map[i][j] < b[j]){
					ans = 0;
					break;
				}
			}
		}
		if(ans) printf("Case #%d: YES\n",cas);
		else printf("Case #%d: NO\n",cas);

	}
	return 0;
}