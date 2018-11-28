#include <bits/stdc++.h>

using namespace std;

double solve()
{
	double c, f, x;
	
	scanf("%lf %lf %lf", &c, &f, &x);
	
	double prod = 2.0;
	double req = 0;
	double ans = 1e18;
	
	for (int i = 0; i < 10000; i++){
		ans = min(ans, req + x / prod);
		req += c / prod;
		prod += f;
	}
	return (ans);
}

int main()
{
	int Tnum;
	
	scanf("%d", &Tnum);
	
	for (int i = 0; i < Tnum; i++)
		printf("Case #%d: %lf\n", i + 1, solve());
	
	return (0);
}