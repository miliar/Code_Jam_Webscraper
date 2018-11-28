#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

#define FILE_NAME "B-small-attempt0"
#define ULL unsigned long long

char buffer[2048];

double cost, incR, target;

double buyX(int n)
{
	if(n==0)
		return target/2.0;
	
	double t = 0;
	double curR = 2.0;
	for(int i=0;i<n;i++)
	{
		t+=cost/curR;
		curR+=incR;
	}
	return (t+target/curR);
}

double solve(double &target, double &curR)
{
	double nb = buyX(0);
	double min = nb;
	int i=1;
	while(1)
	{
		double temp = buyX(i);
		if(temp>min)
			break;
		else
		{
			if(temp<min)
				min = temp;
		}
		i++;
	}
	return min;
}

int main()
{
	sprintf(buffer, "%s.in", FILE_NAME);
	freopen(buffer, "r", stdin);
	sprintf(buffer, "%s.out", FILE_NAME);
	freopen(buffer, "w", stdout);

	int case_num;
	int i=1;
	scanf("%d", &case_num);
	while(i<=case_num)
	{
		printf("Case #%d: ", i);
		
		scanf("%lf%lf%lf", &cost, &incR, &target);

		double curR = 2;

		printf("%lf", solve(target, curR));

		printf("\n");
		i++;
	}
		
	return 0;
}