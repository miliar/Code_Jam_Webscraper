#include <cstdio>
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
	freopen ("aain.txt","r",stdin);
	freopen ("aaout.txt","w",stdout);
	int tc, t=0;
	scanf("%d", &tc);
	double c,r,  f, x,c_time, p_time, time;
	while(tc--)
	{
		t++;
		r= 2.0000000;
		scanf("%lf%lf%lf", &c, &f, &x);
		
		if(x<=c)
		{
			printf("Case #%d: %.7lf\n",t, x/r);
		}
		else
		{
			p_time= x/r;
			c_time= x/r;
			time= c/r;
			while(c_time<=p_time)
			{
				p_time=c_time;
				r+=f;
				c_time= x/r+ time;
				time+= c/r;
			}
			printf("Case #%d: %.7lf\n",t, p_time);
		} 
	}
	return 0;
}
