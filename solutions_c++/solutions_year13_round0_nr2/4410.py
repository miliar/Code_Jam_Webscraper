#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int tt;
int n,m;
int a[100][100];
bool f[100][100];

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
				scanf("%d",&a[i][j]);
		memset(f,false,sizeof(f));
		for (int i=0;i<n;++i) {
			int now=0;
			for (int j=0;j<m;++j)
				now=max(now,a[i][j]);
			for (int j=0;j<m;++j)
				if (a[i][j]==now) f[i][j]=true;
		}
		for (int j=0;j<m;++j) {
			int now=0;
			for (int i=0;i<n;++i)
				now=max(now,a[i][j]);
			for (int i=0;i<n;++i)
				if (a[i][j]==now) f[i][j]=true;
		}
		bool flag=true;
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
				if (!f[i][j]) flag=false;
		printf("Case #%d: ",ii);
		if (flag) printf("YES\n");
		else printf("NO\n");
	}
}
