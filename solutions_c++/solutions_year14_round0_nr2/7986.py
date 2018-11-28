#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	freopen("cookies.in", "r", stdin);
	freopen("cookies.out", "w", stdout);
	scanf("%d", &T);
	for (int Cs=1; Cs<=T; ++Cs)
	{
		double C, F, X, now = 0, ans = 1E18;
		scanf("%lf%lf%lf", &C, &F, &X);
		for (int j=0; j<=100005; ++j)
		{
			ans = min(ans, now + X / (2 + j * F));
			now = now + C / (2 + j * F);
		}
		printf("Case #%d: %.7lf\n", Cs, ans);
	}
	fclose(stdin); fclose(stdout);
	return 0;
}

