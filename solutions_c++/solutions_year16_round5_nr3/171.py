#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<functional>

using namespace std;

#define mp make_pair
#define pb push_back
#define fi first
#define se second

typedef long long llint;

struct arr
{
	int x,y,z;
} a[1010],b[1010];

int n, S, ft[1010];
int len;
pair<int, pair<int, int> > lis[1010 * 1010];

int fa(int x)
{
	if (ft[x] == x) return x;
	return ft[x]=fa(ft[x]);
}

#define sqr(x) ((x) * (x))
inline int dist(const arr&a, const arr&b)
{
	return sqr(a.x - b.x) + sqr(a.y-b.y) + sqr(a.z-b.z);
}

int main()
{
	freopen("C.in","r",stdin);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d",&n, &S);
		for(int i=0;i<n;i++) scanf("%d%d%d%d%d%d",&a[i].x,&a[i].y,&a[i].z,&b[i].x,&b[i].y,&b[i].z),ft[i]=i;
		len=0;
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++) lis[len++]=mp(dist(a[i],a[j]), mp(i,j));
		sort(lis,lis+len);
		double value = 0;
		for(int i=0;i<len;i++)
		{
			int x = fa(lis[i].se.fi), y = fa(lis[i].se.se);
			ft[x]=y;
			if (fa(0) == fa(1))
			{
				value = lis[i].fi;
				break;
			}
		}
		printf("Case #%d: %.7f\n", tt, sqrt(value));
	}
	
	return 0;
}