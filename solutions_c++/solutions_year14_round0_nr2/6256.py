#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<set>
#include<vector>
using namespace std;
main()
{
	int cases;
	scanf("%d",&cases);
	for(int c1=1;c1<=cases;c1++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double ret=0.0,ret1=2.0;
		while(1)
		{
			double time1;
			time1=x/ret1;
			double time2=c/ret1;
			double temp=ret1+f;
			time2+=x/temp;
			//cout<<"time1 "<<time1<<" time2 "<<time2<<"\n";
			if(time1<=time2)
			{
				ret+=time1;
				break;
			}
			ret+=c/ret1;
			ret1+=f;
		}
		printf("Case #%d: %lf\n",c1,ret);
	}
}
