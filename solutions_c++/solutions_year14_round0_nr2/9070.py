#include<cstdio>
#include<cmath>
#define D long double
#define eps 1e-9

int cmp(D a, D b)
{
	if(fabs(a-b) < eps) return 0;
	if(a<b) return -1;
	return 1;
}

int main()
{
	int t;scanf("%d",&t);
	for(int i=1;i<=t;++i)
	{
		printf("Case #%d: ",i);
		D c, f, x;
		scanf("%Lf%Lf%Lf", &c, &f, &x);
		D ans = 0, r = 2; 
		while(cmp(x/r, c/r+x/(f+r)) > 0 )
		{
			ans += c/r;
			r += f;
		}
		ans += x/r;
		printf("%.10Lf\n", ans);
	}
	return 0;
}
