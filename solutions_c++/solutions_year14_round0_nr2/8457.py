#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
#define D double


int main()
{
	int t;
	scanf("%d", &t);
	for(int qwe=1; qwe<=t; qwe++)
	{
		D c, f, x, cookie=2.0, time=1000000.0, tmp=0.0;
		bool b=1;
		scanf("%lf%lf%lf", &c, &f, &x);
		while(b)
		{
			if(time<tmp+x/cookie) b=0;
			else
			{
				time=tmp+x/cookie;
				tmp+=c/cookie;
				cookie+=f;
			}
		}
		printf("Case #%d: %lf\n", qwe, time);
	}
	return 0;
}
