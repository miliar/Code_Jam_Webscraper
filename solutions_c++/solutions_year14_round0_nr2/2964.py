#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int T, cases = 0;
double c, f, x, per, t;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d", &T);
	while(T--)
	{
		scanf("%lf%lf%lf", &c, &f, &x);
		per = 2.0;
		t = 0;
		while(1)
		{
			if(x / per > c / per + x / (per + f))
			{
				t += c / per;
				per += f;
			}
			else
			{
				t += x / per;
				break;
			}
		}
		printf("Case #%d: %lf\n", ++cases, t);
	}
	return 0;
}
