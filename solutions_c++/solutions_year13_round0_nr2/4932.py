#include <cstdio>

int trawnik[111][111];
int kolumnaMax[111];
int wierszMax[111];

void clear() {
	for(int i=0; i<111;++i) 
		kolumnaMax[i]=wierszMax[i]=-1;
}

int main() {
	int T,t=0;
	scanf("%d", &T);
	while(t++<T) {
		int n,m;
		clear();
		scanf("%d%d",&n,&m);
		for(int i=0; i<n; ++i) {
			for(int j=0; j<m; ++j) {
				scanf("%d", &(trawnik[i][j]));
				if(kolumnaMax[j]<trawnik[i][j])
					kolumnaMax[j]=trawnik[i][j];
				if(wierszMax[i]<trawnik[i][j])
					wierszMax[i]=trawnik[i][j];
			}
		}
		bool dobrzeZaprojektowany=true;
		for(int i=0; i<n; ++i) {
			for(int j=0; j<m; ++j) {
				if(trawnik[i][j]<kolumnaMax[j] &&
				   trawnik[i][j]<wierszMax[i]) {
					dobrzeZaprojektowany=false;
					i=n;
					break;
				}
			}
		}
		if(dobrzeZaprojektowany) {
			printf("Case #%d: YES\n",t);
		} else {
			printf("Case #%d: NO\n",t);
		}
	}
	return 0;
}

