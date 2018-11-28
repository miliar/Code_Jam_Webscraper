#include <cstdio>

int table[109][109];

int main(){	
	int t,n,m;
	scanf("%d",&t);
	int caso = 1;
	while(t--){
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				scanf("%d",&table[i][j]);
			}
		}

		bool error = false;

		for(int i=0;i<n;i++){
			for(int j=0;j<m&&!error;j++){
				bool failY = false;
				bool failX = false;
				int v = table[i][j];
				for(int k=0;k<n && failY==false;k++){
					if ( table[k][j] > v ){
						failY = true;
					}
				}
				for(int k=0;k<m && failX==false;k++){
					if ( table[i][k] > v ){
						failX = true;
					}
				}

				if (failX && failY){
					error = true;
				}
			}
		}

		if ( error ){
			printf("Case #%d: NO\n",caso);
		}else{
			printf("Case #%d: YES\n",caso);
		}
		caso++;
	}
	return 0;
}