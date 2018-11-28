#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	for (int ri=0;ri<T;ri++)
	{
		int n;
		double nao[2000],ken[2000];
		scanf("%d",&n);
		for (int i=0;i<n;i++)
			scanf("%lf",&nao[i]);
		for (int i=0;i<n;i++)
			scanf("%lf",&ken[i]);
		sort(nao,nao+n);
		sort(ken,ken+n);
		int np,kp,w1,w2;
		np=kp=w1=w2=0;
		for(;np<=n-1;np++,kp++)
		{
			while (np<=n-1&&nao[np]<ken[kp]) np++;
			if (np<=n-1&&nao[np]>ken[kp])w1++;
		}
		np=kp=0;
		for (;kp<=n-1;np++,kp++)
		{
			while (kp<=n-1&&nao[np]>ken[kp]) kp++;
			if (kp<=n-1&&nao[np]<ken[kp]) w2++;
		}
		/*for (int i=0;i<n;i++)
		printf("%.3lf\n",nao[i]);*/
		printf("Case #%d: %d %d\n",ri+1,w1,n-w2);
	}
}
