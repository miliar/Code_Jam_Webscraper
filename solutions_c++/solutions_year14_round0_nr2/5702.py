#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

const double eps = 1e-7;

double c,f,x;
double ans;
double v;
double now;

int main()
{
	int t;
	scanf("%d",&t);
	int cas = 0;
	while (t--)
	{
		cin>>c>>f>>x;
		v = 2.0;
		ans = x / v;
		now = 0;
		while (true)
		{
			now += c / v;
			v += f;
			long double tmp = now + x / v;
			if (eps < ans - tmp)
				ans = tmp;
			else
				break;
		}
		printf("Case #%d: ",++cas);
		printf("%.7lf\n",ans);
	}
	return 0;
}
