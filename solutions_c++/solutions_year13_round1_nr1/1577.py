#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
const double PI = 22/7;
int main()
{
	freopen("input1.in","r",stdin);
	freopen("output1.out","w",stdout);
	int test,i,j,ans;
	long long r,t;
	double area, prevarea,blackarea, blackremain;
	scanf("%d", &test);
	for(int z = 1;z <= test;z++)
	{
		scanf("%lld %lld",&r,&t);
		ans = 0;
		blackremain = t*1.0;
		while(true)
		{
			prevarea = PI * r * r;
			blackarea = PI * (r+1) * (r+1) - prevarea;
			blackremain = blackarea/PI;
			if(t - blackremain >= 0)
				{
					t -= blackremain;
					r+=2;
					ans++;
				}
			else
				break;
		}
		printf("Case #%d: %d\n",z,ans);
	}
	return 0;
}
