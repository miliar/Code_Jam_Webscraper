#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	int T,t;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	
	for (int t = 1; t<=T; ++t)
	{
		double C,F,X;
		scanf("%lf %lf %lf", &C, &F, &X);
		
		double v = 2;
		double time = 0;
		while (X * F > C * (v + F)){
			time += C / v;
			v += F; 
		}
		
		time += X / v;
		printf("Case #%d: %.7lf\n", t, time);
	}
	return 0;
}
