#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

double F,X,C;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large-out.out","w",stdout);
	
	int test;
	scanf("%d",&test);
	for(int i=1; i<=test; i++)
	{
		cin>>C>>F>>X;
	
		double time = 0;
		double ans = 100000;
		double get_cookies = 2;

		while(ans > time)
		{
			ans = min(ans, time + X/get_cookies);
			time += C/get_cookies;
			get_cookies += F;
		}
		printf("Case #%d: %.15lf\n",i,ans);
	}


return 0;
}