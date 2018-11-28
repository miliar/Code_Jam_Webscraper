#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <ctime>
#include <map>
#define fi first
#define se second
#define PA pair<int,int>
#define VI vector<int>
#define VP vector<PA >
#define mk(x,y) make_pair(x,y)
#define N 10010
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
int i,j,k,n,m,te,T;
int a[N],an[N];
map<int,int> b;
int main() {
	freopen("log.in","r",stdin);
	freopen("log.out","w",stdout);
	scanf("%d",&T);
	For(te,1,T) {
		scanf("%d",&n);
		For(i,1,n) scanf("%d",&a[i]);
		b.clear();
		For(i,1,n) scanf("%d",&k),b[a[i]]+=k;
		sort(a+1,a+n+1);
		int t=0;
		b[0]--;
		for (i=1;i<=n;) if (!b[a[i]]) i++;
		else {
			//printf("%d %d %d\n",i,a[i],b[a[i]]);
			int nn=(1<<t)-1;
			For(j,0,nn) {
				int s=a[i];
				For(k,1,t) if (j>>k-1&1) s+=an[k];
				b[s]--;
			}
			an[++t]=a[i];
		}
		printf("Case #%d: ",te);
		For(i,1,t) printf("%d%c",an[i],i==t?'\n':' ');
	}
	return 0;
}
