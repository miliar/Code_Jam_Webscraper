#include <cstdio>
#include <set>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

void Solve()
{
	double C, F, X, ans, speed;
	scanf("%lf%lf%lf", &C, &F, &X);
	speed = 2;
	ans = X/speed;
	double t = 0;
	while(t < ans){
		t += C/speed;
		speed += F;
		double tmp = t+X/speed;
		if(ans > tmp)
			ans = tmp;
		else if(fabs(ans-tmp)<1e-7)
			break;
	}
	printf("%.7f\n", ans);
}

int main()
{
	freopen("B-large.in", "r", stdin);
//	freopen("large.out", "w", stdout);
	int nCase;
	scanf("%d", &nCase);
	for(int i = 1; i<=nCase; ++i){
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
