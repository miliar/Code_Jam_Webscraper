#include<stdio.h>
int a[101][101];
bool f[101][101];
main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,n,m,min,x,y;
	bool flg;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				scanf("%d",&a[i][j]);
				f[i][j]=false;
			}
		}
		while(1){
			min=101;
			for(int i=0;i<n;i++){
				for(int j=0;j<m;j++){
					if(a[i][j]<min&&!f[i][j]){
						min=a[i][j];
						x=i;
						y=j;
					}
				}
			}
			if(min==101) break;
			flg=true;
			for(int i=0;i<n;i++){
				if(!f[i][y]&&a[i][y]!=min){
					flg=false;
					break;
				}
			}
			if(flg){
				for(int i=0;i<n;i++) f[i][y]=true;
				continue;
			}
			flg=true;
			for(int j=0;j<m;j++){
				if(!f[x][j]&&a[x][j]!=min){
					flg=false;
					break;
				}
			}
			if(flg){
				for(int j=0;j<m;j++) f[x][j]=true;
				continue;
			}
			break;
		}
		flg=true;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(!f[i][j]){
					flg=false;
					break;
				}
			}
			if(flg==false) break;
		}
		if(flg) printf("Case #%d: YES\n",t);
		else printf("Case #%d: NO\n",t);
	}
}
