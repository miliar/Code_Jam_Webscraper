#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <cstdlib>
#include <map>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double cur_rate=2.0,t=0;
		while(1)
		{
			//cout<<t<<": \n" ;
			double t1=x/cur_rate;
			double t2=(c/cur_rate)+(x/(cur_rate+f));
			if(t2<=t1)
			{
			//	cout<<t1<<" "<<t2<<"\n";
				t+=(c/cur_rate);				
				cur_rate+=f;
				
			}
			else
			{
				t+=t1;
				break;
			}
		}
		printf("Case #%d: %lf\n",i+1,t);
		
	}
}
