#include <cstdio>
#include <cstring>
#include <cfloat>
#include <algorithm>
using namespace std;

double C,F,X;

double
goal (int i)
{
	return X / (2 + i*F);
}

double
farm (int i)
{
	return C / (2 + i*F);
}

int
main ()
{
	freopen("Bl.in","r",stdin);
	freopen("Bl.out","w",stdout);
	int t;
	scanf ("%d", &t);
	for (int tc = 1; tc <= t; tc ++){
		scanf ("%lf %lf %lf",&C, &F, &X);
		
		double rate = 2, ans = 0;
		int i = 0;
		while (1){
			double case1 = goal (i);
			double case2 = farm (i) + goal (i+1);
			if (case1 < case2){
				ans += goal (i);
				break;
			}else{
				ans += farm (i);
				i ++;
			}
		}
		printf ("Case #%d: %.7lf\n", tc, ans);
	}
	return 0;
}