//the queen problem
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	freopen("input.txt","r",stdin);
	int t;
	int o=0;
	double c,f,x;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		double ti=0;
		double curx=0,curspeed=2;
		double t1=0,t2=0;
		while(1)
		{
			t1=x/curspeed;
			t2=c/curspeed+x/(curspeed+f);
			if(t2<t1)
			{
				ti+=c/curspeed;
				curspeed+=f;
			}
			else
			{
				ti+=t1;
				break;

			}
		}
		
		printf("Case #%d: %.7lf\n",++o,ti);
	}
	
	return 0;
}