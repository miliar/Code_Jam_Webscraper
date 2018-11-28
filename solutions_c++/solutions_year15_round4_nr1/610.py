#include <cstdio>

char a[100][101];
int u[100][100];
int d[100][100];
int l[100][100];
int r[100][100];
int n,m;

int cal() {
	int i,j,tmp,ans=0;
	for (i=0;i<n;i++) {
		tmp=-1;
		for (j=0;j<m;j++) {
			l[i][j]=tmp;
			if (a[i][j]!='.') tmp=j;
		}
		tmp=-1;
		for (j=m-1;j>=0;j--) {
			r[i][j]=tmp;
			if (a[i][j]!='.') tmp=j;
		}
	}
	for (j=0;j<m;j++) {
		tmp=-1;
		for (i=0;i<n;i++) {
			u[i][j]=tmp;
			if (a[i][j]!='.') tmp=i;
		}
		tmp=-1;
		for (i=n-1;i>=0;i--) {
			d[i][j]=tmp;
			if (a[i][j]!='.') tmp=i;
		}
	}
	for (i=0;i<n;i++) {
		for (j=0;j<m;j++) {
			if (a[i][j]!='.') {
				if (l[i][j]==-1&&r[i][j]==-1&&u[i][j]==-1&&d[i][j]==-1) return -1;
				if ((a[i][j]=='^'&&u[i][j]==-1)
						||(a[i][j]=='v'&&d[i][j]==-1)
						||(a[i][j]=='<'&&l[i][j]==-1)
						||(a[i][j]=='>'&&r[i][j]==-1))
					ans++;
			}
		}
	}
	return ans;
}

int main() {
	int t,tt,i;
	scanf("%d",&t);
	for (int tt=1;tt<=t;tt++) {
		scanf("%d%d",&n,&m);
		for (i=0;i<n;i++) scanf("%s",a[i]);
		int ans=cal();
		printf("Case #%d: ",tt);
		if (ans==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}
