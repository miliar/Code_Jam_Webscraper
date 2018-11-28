#include <cstdio>

using namespace std;

int main()
{
	int tc;
	double c,f,x;
	scanf("%d",&tc);
	for(int k=1;k<=tc;k++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		printf("Case #%d: ",k);
		double i =0;
		double j =2;
		while(x/j>=c/j+x/(j+f))
		{
			i+=c/j;
			j+=f;
		}
		printf("%.7lf\n",(i+x/j));
	}

	return 0;
}