//Problem 2 贪心 
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int main()
{
	int T;
	double C;
	double F;
	double X;
	int cnt;
	//freopen("C:\\Users\\lovesunmoon\\Desktop\\Problem 2in.txt","r",stdin);
   	//freopen("C:\\Users\\lovesunmoon\\Desktop\\Problem 2out.txt","w",stdout);
	scanf("%d",&T);
	for(cnt=1;cnt<=T;cnt++)
	{
		double rate=2.0;
		double ans=0.0;
		scanf("%lf%lf%lf",&C,&F,&X);
		if(X<=C)
		ans=X/2.0;
		if(X>C)
		{
			while(X/rate>C/rate+X/(rate+F))//rate是当前的速率，rate+F是达到下一个阶段的速率 
			{
				ans+=C/rate;
				rate+=F; 
			} 
			ans+=X/rate;
		}
		printf("Case #%d: %lf\n",cnt,ans);
	}
	return 0;
}