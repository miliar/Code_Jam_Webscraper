#include<cstdio>

using namespace std;

int main()
{
	freopen("input2.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,t1;
	scanf("%d",&t);
	t1=t;
	while(t--)
	{
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);
		double cps1=2,cps2=2;
		double cost11=0,cost21=0;
		double cost1=x/cps2;
		double cost2=c/cps2;
		cost21=cost2;
		cps2+=f;
		cost2=cost2+(x/cps2);
		while(1)
		{
			if(cost1<cost2) 
			{
				printf("Case #%d: %.7lf\n",t1-t,cost1);
				break;
			}
			else
			{
				cost1=cost2;
				//cost21=cost2;
				cost2=cost21+c/cps2;
				cost21=cost2;
				cps2+=f;
				cost2=cost2+(x/cps2);
			}
		}
	}
	return 0;
}
