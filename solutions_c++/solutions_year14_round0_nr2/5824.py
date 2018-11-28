#include <stdio.h>
#include <algorithm>
using namespace std;

typedef long double real;

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int t = 0; t < T; t++)
	{
		real rate = 2.0L, C, F, X;
		scanf("%Lf %Lf %Lf", &C, &F, &X);
		
		real time = X / rate;
		real calc = 0;
		for(int i = 0; i < X + 5; i++)
		{
			calc += C / rate;
			rate += F;
			time = min(time, calc + X / rate);
		}
		
		printf("Case #%d: %.7Lf\n", t + 1, time);
	}
	
	return 0;
}
