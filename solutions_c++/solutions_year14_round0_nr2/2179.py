#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;
int T;
double c,f,x,r,ans,now;
int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&T);
	for(int t = 1 ; t <= T ;++ t)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		r = 2;
		ans = x / r;
		now = 0;
		while(1)
		{
			now += c / r;
			r += f;
			if (now + x / r <= ans)
				ans = now + x / r;
			else
			break;
		}
		printf("Case #%d: %.7lf\n",t,ans);
	}
}