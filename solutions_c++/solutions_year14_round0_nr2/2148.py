#include <stdio.h>
#include <iostream>
FILE *in = fopen("B-large.in", "r");
FILE *out = fopen("output.txt", "w");

int n = 1;
void testCase()
{
	double C, F, X;
	fscanf(in, "%lf %lf %lf", &C, &F, &X);
	double &farmCost = C;
	double &extra = F;
	double &goal = X;

	double increasing = 2.0;
	double totalFarmCost = 0.0;
	double minCost = goal / increasing;
	double cost;
	while(1)
	{
		cost = goal / increasing + totalFarmCost;
		if(cost <= minCost)
		{
			minCost = cost;
		}
		else
		{
			break;
		}
		totalFarmCost = totalFarmCost + farmCost / increasing;
		increasing = increasing + extra;
		
	}
	fprintf(out, "Case #%d: %.7lf\n",n++,minCost);
}
int main(void)
{
	int T;
	fscanf(in, "%d", &T);
	while(T--)
	{
		testCase();
	}
}