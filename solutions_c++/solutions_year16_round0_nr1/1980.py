#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>

using namespace std;
#define rep(i,a,b) for (int i=(a);i<=(b);i++)
#define repd(i,a,b) for (int i=(a);i>=(b);i--)

const int maxn=1000020;
int ans[maxn];
int n,m;
bool ft[20];


int main() {
	freopen("a.out","w",stdout);
	int T;scanf("%d\n",&T);
	rep(t,1,T) {
		printf("Case #%d: ",t);
		scanf("%d\n",&n);
		if (n==0) {
			puts("INSOMNIA");
			continue;
		}
		if (ans[n]!=0) {
			printf("%d\n",ans[n]);
			continue;
		}
		m=n;
		rep(i,0,9) ft[i]=false;
		while (1) {
			int tmp=0,k=n;
			ans[m]=n;
			n+=m;
			while (k) ft[k%10]=true,k/=10;
			rep(i,0,9)
				tmp+=ft[i];
			if (tmp==10)
				break;
		}
		printf("%d\n",ans[m]);
	}
	return 0;
}
