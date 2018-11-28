#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <ctime>
#include <queue>
#include <set>
#include <map>
#define fi first
#define se second
#define PA pair<int,int>
#define VI vector<int>
#define VP vector<PA >
#define mk(x,y) make_pair(x,y)
#define int64 long long
#define db double
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
int i,j,k,n,m,an,t;
int p[100],f[100];
VI a;
set<VI> Set;
inline bool ju(VI a) {
	int i,j,k;
	For(i,2,10) {
		int f=0;
		For(k,1,t) {
			int s=0;
			For(j,0,n-1) s=(s*i+a[j])%(p[k]);
			if (s==0) {
				f=1;
				break;
			}
		}
		if (!f) return 0;
	}
	return 1;
}
inline void gao(VI a) {
	int i,j,k;
	For(i,2,10) {
		int f=0;
		For(k,1,t) {
			int s=0;
			For(j,0,n-1) s=(s*i+a[j])%(p[k]);
			if (s==0) {
				printf(" %d",p[k]);
				break;
			}
		}
	}
}
int main() {
	freopen("jamcoin.out","w",stdout);
	{
		For(i,2,90) for (j=i+i;j<=90;j+=i) f[j]=1;
		For(i,3,90) if (!f[i]) p[++t]=i;
	}
	scanf("%d%d",&n,&m);
	printf("Case #1:\n");
	for (;m;) {
		a.clear();
		a.resize(n);
		a[0]=a[n-1]=1;
		For(i,1,n-2) a[i]=rand()&1;
		if (Set.count(a)) continue;
		if (ju(a)) {
			Set.insert(a);
			m--;
			cerr<<m<<endl;
			continue;
		}
	}
	//printf("yes\n");
	for (auto j:Set) {
		For(i,0,n-1) printf("%d",j[i]);
		gao(j);
		printf("\n");
	}
	return 0;
}
