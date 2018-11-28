#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for (int i = a;i <= b;i ++)

using namespace std;

const int maxn = 10005;
int T,N,S,a[maxn];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	fo(cs,1,T)
	{
		scanf("%d%d",&N,&S);
		fo(i,1,N) scanf("%d",&a[i]);
		sort(a+1,a+1+N);
		int ans = 0;
		while (1)
		{
			bool empty = 1;
			for (int i = N;i;i --)
				if (a[i] > 0)
				{
					empty = 0;
					break;
				}
			if (empty) break;
			int rest = S, cnt = 0;
			for (int i = N;i;i --)
				if (a[i] > 0)
					if (rest >= a[i])
					{
						rest -= a[i];
						a[i] = 0;
						cnt ++;
						if (cnt == 2) break;
					}
			ans ++;
		}
		printf("Case #%d: ",cs);
		printf("%d\n",ans);
	}
	return 0;
}
