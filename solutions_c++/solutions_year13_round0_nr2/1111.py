#include<cstdio>
#include<algorithm>
using namespace std;
int n,m;
int dat[128][128];
int res[128][128];
int row[128], col[128];
int main() {
	int e = 0, T;
	scanf("%d", &T);
	while(T--) {
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;++i) row[i] = -1;
		for(int j=0;j<m;++j) col[j] = -1;

		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j) {
				scanf("%d",&dat[i][j]);
				res[i][j] = 100;
				row[i] = max(row[i], dat[i][j]);
				col[j] = max(col[j], dat[i][j]);
			}
		for(int i=0;i<n;++i) {
			for(int j =0;j<m;++j) {
				res[i][j]=min(res[i][j], row[i]);
				res[i][j]=min(res[i][j], col[j]);
			}
		}
		int flag = 0;
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				if(res[i][j] != dat[i][j]) {
					flag = 1;
					break;
				}
		printf("Case #%d: %s\n", ++e, flag ? "NO" : "YES");
	}
	return 0;
}
