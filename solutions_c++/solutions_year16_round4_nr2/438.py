#include <cstdio>
#include <cstring>
#include <algorithm>
#define fo(i,a,b) for (int i = a;i <= b;i ++)

using namespace std;

int T,N,K;
double ans,cur[205],p[205],f[205][205];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&T);
	fo(cs,1,T)
	{
		scanf("%d%d",&N,&K);
		fo(i,1,N) scanf("%lf",&p[i]);
		printf("Case #%d: ",cs);
		sort(p+1,p+1+N);
		ans = 0.0;
		fo(i,0,K)
		{
			fo(j,1,i) cur[j] = p[j];
			fo(j,i+1,K) cur[j] = p[N-K+j];
			fo(i,0,K) fo(j,0,K) f[i][j] = 0.0;
			f[0][0] = 1.0;
			fo(i,0,K-1)
				fo(j,0,i)
				{
					f[i+1][j] += cur[i+1] * f[i][j];
					f[i+1][j+1] += (1-cur[i+1]) * f[i][j];
				}
			ans = max(f[K][K/2],ans);
		}
		printf("%.8f\n",ans);
	}
	return 0;
}
