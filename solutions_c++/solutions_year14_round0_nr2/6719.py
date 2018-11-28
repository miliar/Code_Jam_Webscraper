#include<iostream>
#include<vector>
#include<cmath>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		double c,f,x;
		double ini = 2.0;
		cin>>c>>f>>x;
		double ans=0.0;
		
			
		
		while(1)
		{
			double buy_t = c/ini;
			double goal_t = x/(ini+f);
			double time_buy = buy_t+goal_t;
			double time_goal = x/ini;
			//cout<<x<<" "<<ini<<endl;
			//cout<<time_buy<<" "<<time_goal;
			if(time_buy <time_goal)
			{
				ans = ans + buy_t; 
				ini = ini+f;
				continue;
			}
			else
			{
				ans = ans + time_goal;
				break;
			}
			
		}
		cout<<"Case #"<<i+1<<":"<<" ";
		printf("%.7f\n",ans);
	}
	cin>>t;
	return 0;
}