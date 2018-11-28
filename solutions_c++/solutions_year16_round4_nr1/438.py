#include <cstdio>
#include <cstring>
#include <algorithm>
#define fo(i,a,b) for (int i = a;i <= b;i ++)

using namespace std;

int T,N,M,R,P,S;
int a[3],b[3],ans[20000],ret[20000];
bool ok;

bool Cmp(int *a,int *b,int len)
{
	for (int i = 0;i < len;i ++)
	{
		if (a[i] < b[i]) return 1;
		if (a[i] > b[i]) return 0;
	}
	return 0;
}

bool Check()
{
	memset(b,0,sizeof b);
	fo(i,1,M) b[ret[i]] ++;
	fo(i,0,2) if (b[i] != a[i]) return 0;
	return 1;
}

void Work(int l,int r,int cur)
{
	if (l == r)
	{
		ret[l] = cur;
		return;
	}
	int mid = (l + r) / 2;
	Work(l,mid,cur);
	Work(mid+1,r,(cur+1)%3);
	if (Cmp(ret+mid+1,ret+l,r-mid))
		fo(i,l,mid) swap(ret[i],ret[i-l+mid+1]);
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	fo(cs,1,T)
	{
		scanf("%d%d%d%d",&N,&a[1],&a[0],&a[2]);
		M = 1 << N;
		printf("Case #%d: ",cs);
		ok = 0;
		fo(i,0,2)
		{
			Work(1,M,i);
			if (Check() && (!ok||Cmp(ret+1,ans+1,M)))
			{
				memcpy(ans,ret,sizeof ans);
				ok = 1;
			}
		}
		if (ok)
		{
			fo(i,1,M)
			{
				if (ans[i] == 0) printf("P");
				if (ans[i] == 1) printf("R");
				if (ans[i] == 2) printf("S");
			}
			printf("\n");
		} else printf("IMPOSSIBLE\n");
	}
	return 0;
}

