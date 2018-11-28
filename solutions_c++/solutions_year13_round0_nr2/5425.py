#include <cstdio>
int a[11][11];
bool c[11][11];
int main() {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	int n,m;
	scanf("%d",&t);
	for (int tc=1; tc<=t ;tc++) {
		scanf("%d %d",&n,&m);
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++)
				scanf("%d",&a[i][j]);
		bool ans=false;
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				c[i][j] = false;
			}
		}
		for (int i=0; i<n; i++) {
			bool all1 = true;
			for (int j=0; j<m; j++) {
				if (a[i][j] ==2 ) all1 = false;
			}
			if (all1) {
				for (int j=0; j<m; j++) c[i][j] = true;
			}
		}
		for (int j=0; j<m; j++) {
			bool all1 = true;
			for (int i=0; i<n; i++) {
				if (a[i][j] ==2 ) all1 = false;
			}
			if (all1) {
				for (int i=0; i<n; i++) c[i][j] = true;
			}
		}
		ans = true;
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				if (a[i][j] == 1 && c[i][j] == false) ans = false;
			}
		}
		printf("Case #%d: %s\n",tc,ans?"YES":"NO");
	}
	return 0;
}