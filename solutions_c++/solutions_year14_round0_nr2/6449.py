#include<iostream>
using namespace std;
int a[4];
int b[4];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for(int ii = 1; ii <= tt; ii++)
	{
		double c, f, x, d = 2.0;
		scanf("%lf %lf %lf", &c, &f, &x);
		double ans = 0;
		int n = (int)(x/c - 2/f);
		for(int i = 1; i <= n; i++)
		{
			ans += c/d;
			d += f;
		}
		ans += x/d;
		printf("Case #%d: %.9lf\n", ii, ans);
	}
	return 0;
}