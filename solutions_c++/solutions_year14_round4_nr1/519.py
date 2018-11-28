#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#define N 10010
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
int i,j,k,n,m,test,T,an;
int a[N],b[N];
int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	For(test,1,T) {
		printf("Case #%d: ",test);
		scanf("%d%d",&n,&m);
		For(i,1,n) scanf("%d",&a[i]);
		sort(a+1,a+n+1); an=0;
		j=n;
		For(i,1,n) if (b[i]!=test) {
			for (;j>i&&a[i]+a[j]>m;j--);
			if (i<j) b[j]=test,j--;
			an++;
		}
		printf("%d\n",an);
	}
	return 0;
}
