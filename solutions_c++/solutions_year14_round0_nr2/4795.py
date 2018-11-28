#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int test,n,cnt;
double C,F,X,ans;

double calc(int m)
{
	double sum=0;
	for (int i=0; i<m; i++) sum+=C/(2+i*F);
	sum+=X/(2+F*m);
	return sum;
}
int main()
{
	freopen("x.in","r",stdin);
	freopen("x.out","w",stdout);
	scanf("%d",&test);
	while (test--)
	{
		cnt++;
		printf("Case #%d: ",cnt);
		scanf("%lf %lf %lf",&C,&F,&X);
		ans=X/2;
		int i=1;
		while (1)
		{
			double t=calc(i);
			i++;
			if (t<ans) ans=t;
			else break;
		}		
		printf("%.7lf\n",ans);
	}
	//while (1);
}
