#include<cstdio>
#define eps (1e-8)
int main()
{
	//freopen("B-small-attempt1.in","r",stdin);
	//freopen("B_small1.out","w",stdout);
	int t;
	scanf("%d", &t);
	for(int _ = 0; _ < t; ++_)
	{
		double _c,_f,_x;
		scanf("%lf%lf%lf",&_c,&_f,&_x);
		int mCount = 0;
		double totalTime = 0.0;
		while(1)
		{
			if((_x / (2.0 + (mCount + 1) * _f) + (_c / (2.0 + mCount * _f)))
				- (_x / (2.0 + mCount * _f)) >= eps)
			{
				break;	
			}
			totalTime += _c / (2.0 + mCount * _f);
			++mCount;
		}
		totalTime += _x / (2.0 + mCount * _f);
		//printf("%d %.7lf\n", mCount, totalTime);
		printf("Case #%d: %.7lf\n", _ + 1, totalTime);
	}
	return 0;
}
/*
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0
*/
