#include <stdio.h>
#include <string.h>
#include <algorithm>
#define N 101

using namespace std;


int T;

int a[N][N],b[N][N];

int n,m;

int main(void){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	int cc=0;
	while (T--){
		int err=0;

		scanf("%d %d",&n,&m);

		for (int i=0;i<n;i++){
			for (int j=0;j<m;j++) scanf("%d",&a[i][j]);
		}

		for (int h=100;h>0;h--){
			for (int i=0;i<n;i++)for (int j=0;j<m;j++) if (a[i][j]<=h) b[i][j]=1;else b[i][j]=0;

			for (int i=0;i<n;i++) for (int j=0;j<m;j++) if (a[i][j]==h){
				int kol1=0;
				for (int k=0;k<n;k++) kol1+=b[k][j];
				int kol2=0;
				for (int k=0;k<m;k++) kol2+=b[i][k];
				if (kol1<n && kol2<m) err=1;
			}
		}
		cc++;
		printf("Case #%d: ",cc);
		if (err) puts("NO");else puts("YES");
	}
	return 0;
}