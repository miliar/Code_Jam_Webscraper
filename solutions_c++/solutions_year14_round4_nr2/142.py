
#include <bits/stdc++.h>
using namespace std;

int T;
int n;
int a[1024];
int l[1024];
int r[1024];

int main() {
	freopen("inl.txt","r",stdin);
	freopen("outl.txt","w",stdout);
	scanf("%d",&T);
	for (int ww=1;ww<=T;ww++) {
		printf("Case #%d: ",ww);
		scanf("%d",&n);
		int ans=0;
		memset(l,0,sizeof(l));
		memset(r,0,sizeof(r));
		for (int i=1;i<=n;i++) scanf("%d",a+i);
		for (int i=1;i<=n;i++) {
			l[i]=0;
			for (int j=1;j<i;j++)
				if (a[i]<a[j]) l[i]++;
		}
		for (int i=n;i>=0;i--) {
			r[i]=0;
			for (int j=i+1;j<=n;j++)
				if (a[i]<a[j]) r[i]++;
		}
		for (int i=1;i<=n;i++) ans+=min(l[i],r[i]);
		printf("%d\n",ans);
	}
	return 0;
}
