#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int T;
double c,f,x;
#define eps 1e-7
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	scanf("%d",&T);
	double ans = 0;
	double have=0;
	double temp;
	double ext;
	int t=0;
	while(T--)
	{
		t++;
		scanf("%lf%lf%lf",&c,&f,&x);
		printf("Case #%d: ",t);
		ans =0;
		ext = 2;
		while(1)
		{
			double next = c/ext;
			if(ans+next+x/(ext+f)+eps < ans+ x/ext)
			{
				ans+= next;
				ext+=f;
			}
			else 
			{
				ans = ans+x/ext;
				break;
			}
		}
		printf("%.7lf\n",ans);

	}
	return 0;
}
