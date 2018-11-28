#include<cstdio>
#include<algorithm>

using namespace std;

int t;
double C, F, X, ans, pr, time;

int main()
{                               
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%lf%lf%lf", &C, &F, &X);
		pr = 2;
		ans = 1e18;
		time = 0;
		for (int j = 0; j < 1e5; j++)
		{
			ans = min(ans, X / pr + time);
			time += C / pr;
			pr += F;
		}
		printf("Case #%d: %.20lf\n", i + 1, ans);
	}	
	return 0;
}	