#include<cstdio>
#include<algorithm>
using namespace std;

int a[500][500],b[500][500];
int d[500];
int testcase,test,n,m;

int main() {
	int i,j,k,l,t;
	bool flag;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&testcase);
	for (test=1;test<=testcase;test++) {
		scanf("%d%d",&n,&m);
		for (i=1;i<=n;i++)
			for (j=1;j<=m;j++) 
				scanf("%d",&a[i][j]);
		for (i=1;i<=n;i++) {
			t=0;
			for (j=1;j<=m;j++)
				t=max(t,a[i][j]);
			d[i]=t;
		}
		for (j=1;j<=m;j++) {
			t=0;
			for (i=1;i<=n;i++)
				t=max(t,a[i][j]);
			d[j+n]=t;
		}
		for (i=1;i<=n;i++)
			for (j=1;j<=m;j++)
				b[i][j]=100;
		for (k=100;k>=1;k--) {
			for (l=1;l<=n+m;l++)
				if (d[l]==k) {
					if (l<=n) for (j=1;j<=m;j++) b[l][j]=k;
					else for (i=1;i<=n;i++) b[i][l-n]=k;
				}
		}
		flag=true;
		for (i=1;i<=n;i++)
			for (j=1;j<=m;j++)
				if (a[i][j]!=b[i][j]) flag=false;
		printf("Case #%d: ",test);
		if (flag) printf("YES\n");
		else printf("NO\n");
	}
}
