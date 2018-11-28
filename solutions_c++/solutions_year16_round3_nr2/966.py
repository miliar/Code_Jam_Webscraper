#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int b,m,a[10][10],f[20];
bool flag;

void dfs(int p, int q) {
	if (q>b) {
		++p;
		q=p+1;
	}
	if (p==b) {
		if (f[p]==m) {
			flag=1;
			printf("POSSIBLE\n");
			for (int i=1; i<=b; ++i) {
				for (int j=1; j<=b; ++j)
					printf("%d",a[i][j]);
				printf("\n");
			}
		}
	} else {
		if ((!flag) && f[p]+f[q]<=m) {
			f[q]+=f[p];
			a[p][q]=1;
			dfs(p,q+1);
			f[q]-=f[p];
			a[p][q]=0;
		}
		if (!flag) dfs(p,q+1);
	}
}

int main () {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("b.out","w",stdout);
	int TT;
	cin>>TT;
	for (int T=1; T<=TT;++T) {
		cin>>b>>m;
		memset(f,0,sizeof(f));
		flag=0;
		memset(a,0,sizeof(a));
		f[1]=1;
		printf("Case #%d: ", T);
		dfs(1,2);
		if (!flag) printf("IMPOSSIBLE\n");
	}
}
