#include <cstdio>
int a[110][110];
int n,m;
int T,Ti;
int col[110],row[110];
int main() {
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	scanf("%d",&T);
	for(Ti=1;Ti<=T;Ti++) {
		scanf("%d%d",&n,&m);
		int i,j;
		for(i=0;i<n;i++) {
			row[i]=-214748;
		}
		for(i=0;i<m;i++) {
			col[i]=-214748;
		}
		for(i=0;i<n;i++) {
			for(j=0;j<m;j++){
				scanf("%d",&a[i][j]);
				if(row[i]<a[i][j]) {
					row[i]=a[i][j];
				}
				if(col[j]<a[i][j]) {
					col[j]=a[i][j];
				}
			}
		}
		int wb=1;
		for(i=0;i<n;i++) {
			for(j=0;j<m;j++) {
				if(a[i][j]<row[i] && a[i][j]<col[j]) {
					wb=0;
				}
			}
		}
		if(!wb) {
			printf("Case #%d: NO\n",Ti);
		} else {
			printf("Case #%d: YES\n",Ti);
		}
	}
	return 0;
}