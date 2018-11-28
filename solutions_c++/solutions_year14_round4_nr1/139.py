
#include <bits/stdc++.h>
using namespace std;

int T;
int X,n;
int a[16384];

int main() {
	freopen("inl.txt","r",stdin);
	freopen("outl.txt","w",stdout);
	scanf("%d",&T);
	for (int ww=1;ww<=T;ww++) {
		printf("Case #%d: ",ww);
		scanf("%d%d",&n,&X);
		for (int i=1;i<=n;i++) scanf("%d",a+i);
		sort(a+1,a+1+n);
		int lo=1,up=n,ans=0;
		while (lo<=up) {
			if (lo==up) {
				ans++;
				lo++;
				up--;
			}
			else if (a[lo]+a[up]<=X) {
				ans++;
				lo++;
				up--;
			}
			else {
				ans++;
				up--;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
