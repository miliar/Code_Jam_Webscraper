#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
	freopen("b-large.in", "rt", stdin);
	freopen("b-large.out", "wt", stdout);

	int inp;
	int i, j, a1, a2, kase, tmp;
	double c, f, x;
	scanf("%d", &inp);
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		double ans = 0.0;
		double cr = 2.0;
		while(true)
		{
			double tf = c / cr;
			double tx = x / cr;

			double nr = cr + f;
			double ntx = x / nr;

			double ttx = tf + ntx;

			if(ttx <= tx)
			{
				ans += tf;
				cr = nr;
			}
			else
			{
				ans += tx;
				break;
			}

		}
		printf("Case #%d: %.10lf\n", kase, ans);
	}
	return 0;
}