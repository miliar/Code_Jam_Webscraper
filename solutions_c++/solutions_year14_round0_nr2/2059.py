# include<cstdio>
# include<cmath>
# include<algorithm>
using namespace std;
int main()
{
	int i,j,k,l,t;
	double c,f,x,min = 100000000,ans,currRate = 2,temp;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		currRate = 2;
		ans = 0;
		scanf("%lf%lf%lf",&c,&f,&x);
		while(1)
		{
			temp = c/currRate + (x/(currRate+f)); 
			if (temp < (x/currRate))
				ans += c/currRate;
			else
			{
				ans += x/currRate;
				break;
			}
			currRate += f;
		}
		printf("Case #%d: %.7lf\n",k,ans);
	}
	return 0;
}