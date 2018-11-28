#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for (int i = a;i <= b;i ++)

using namespace std;

int T,N,a[1005];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&T);
	fo(cs,1,T)
	{
		scanf("%d",&N);
		fo(i,1,N) scanf("%d",&a[i]);
		int ans = 0,L = 1, R = N;
		fo(k,1,N)
		{
			int M = 0x7fffffff,j;
			fo(i,L,R)
				if (a[i] < M)
				{
					M = a[i];
					j = i;
				}
			if (j-L < R-j)
			{
				for (int i = j;i > L;i --) swap(a[i],a[i-1]), ans ++;
				L ++;
			} else
			{
				for (int i = j;i < R;i ++) swap(a[i],a[i+1]), ans ++;
				R --;
			}
		}
		printf("Case #%d: ",cs);
		printf("%d\n",ans);
	}
	return 0;
}
