#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <ctime>
#define fi first
#define se second
#define PA pair<int,int>
#define VI vector<int>
#define VP vector<PA >
#define mk(x,y) make_pair(x,y)
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
int i,j,k,n,m,T,te;
int a[1010];
int main() {
	freopen("p2.out","w",stdout);
	scanf("%d",&T);
	For(te,1,T) {
		printf("Case #%d: ",te);
		scanf("%d",&n);
		For(i,1,n) scanf("%d",&a[i]);
		int mi=(int)1e9;
		For(i,1,1000) {
			int s=0;
			For(j,1,n) {
				int x=a[j]-i;
				if (x>0) s+=x/i+(x%i>0);
			}
			mi=min(mi,s+i);
		}
		printf("%d\n",mi);
	}
	return 0;
}
