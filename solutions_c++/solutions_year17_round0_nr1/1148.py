#include <cstdio>
#include <cstring>
#include <map>
#include <queue>

using namespace std;
#define rep(i,a,b) for (int i=(a);i<=(b);i++)
#define repd(i,a,b) for (int i=(a);i>=(b);i--)
#define for_iter(i,n) for (__typeof(n.begin())i=n.begin();i!=n.end();++i)

const int maxn=1200;
char s[maxn];
int k,n;

int rev(char x) {
	return x == '+' ? '-' : '+';
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;scanf("%d\n",&T);
	rep(t,1,T) {
		printf("Case #%d: ",t);
		scanf("%s %d\n",s+1,&k);
		n=strlen(s+1);
		int ans=0;
		rep(i,1,n-k+1) {
			if (s[i]=='-') {
				ans++;
				rep(j,i,i+k-1)
					s[j]=rev(s[j]);
			}
		}
		bool ft=true;
		rep(i,n-k+2,n)
			if (s[i]=='-') ft=false;
		if (ft) {
			printf("%d\n",ans);
		} else {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}
