#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>

using namespace std;

int T,tot,n,m,i,j,a[105][105];

inline bool Xun()
{	int i,j,k,A;
	for (i=1;i<=n;i++) for (j=1;j<=m;j++)
	{	A=0;
		for (k=1;k<=m;k++) if (a[i][k]>a[i][j]) A|=1;
		for (k=1;k<=n;k++) if (a[k][j]>a[i][j]) A|=2; if (A==3) return true;
		} return false;
}

int main()
{
//	freopen("B.in","r",stdin);
//	freopen("B.out","w",stdout);
	scanf("%d",&T);
	for (tot=1;tot<=T;tot++)
	{	scanf("%d%d",&n,&m); printf("Case #%d: ",tot);
		for (i=1;i<=n;i++) for (j=1;j<=m;j++) scanf("%d",&a[i][j]);
		if (Xun()) printf("NO\n"); else printf("YES\n");
		}
	return 0;
}
