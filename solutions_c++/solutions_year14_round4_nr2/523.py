#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#define N 1010
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
int i,j,k,n,m,T,test,an;
int a[N],f[N],b[N],c[N][N],s[N];
int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	For(test,1,T) {
		printf("Case #%d: ",test);
		scanf("%d",&n);
		For(i,1,n) scanf("%d",&a[i]),b[i]=a[i];
		sort(b+1,b+n+1);
		For(i,1,n) a[i]=lower_bound(b+1,b+n+1,a[i])-b;
		For(i,1,n)For(j,i+1,n) c[a[i]][a[j]]=test;
		For(i,1,n) {
			s[i]=0;
			For(j,i+1,n) s[i]+=c[j][i]==test;
		}
		f[n]=0; an=n*n;
		For(i,1,n-1) f[i]=n*n;
		for (i=n;i;i--) {
			int sum=0;
			for (j=i-1;j;j--) {
				f[j]=min(f[j],f[i]+s[j]+sum);
				sum+=n-j-s[j];
			}
			an=min(an,f[i]+sum);
		}
		printf("%d\n",an);
	}
	return 0;
}
