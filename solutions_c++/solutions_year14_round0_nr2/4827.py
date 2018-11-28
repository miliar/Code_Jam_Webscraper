#include<cstdio>
using namespace std;


double C,F,X;
double rate;
double total_time;
double min_time;
int end;
void DFS(int);
int main()
{
	int tc;
	scanf("%d",&tc);
	for(int t=1;t<=tc;t++)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		rate=2;
		total_time=0.00000000;
		min_time=2000.00000000;
		end=0;
		DFS(0);
		DFS(1);
		printf("Case #%d: %.7f\n",t,min_time);
	}
}

void DFS(int buy)
{
	if(buy==0)
	{
		double time= X/rate;
		total_time+=time;
		if(min_time>total_time)
			min_time=total_time;
		else
		{
			end=1;
			return;
		}
		total_time-=time;
	}
	else
	{
		double time= C/rate;
		total_time+=time;
		rate+=F;
		DFS(0);
		if(end==1)
			return;
		DFS(1);
	}


}




