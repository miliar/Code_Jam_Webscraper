#include <iostream>


double timetoBuy(double buildingCost, double cocieRate)
{
	return buildingCost/cocieRate;
}

int main()
{
	FILE* fIn, *fOut;
	fopen_s(&fIn, "B-large.in", "rt");
	fopen_s(&fOut, "B-large.out", "wt");

	int T;
	fscanf(fIn, "%d", &T);

	double c, f, x;
	double minTime;
	int iCase = 1;
	while(T--)
	{
		fscanf(fIn, "%lf %lf %lf", &c, &f, &x);
		double currentRate = 2;
		minTime = x/currentRate;
		double buildingTime = 0;
		double nextTime;
		while(1)
		{
			buildingTime += timetoBuy(c, currentRate);
			currentRate += f;
			nextTime = buildingTime + x/currentRate;
			if(nextTime < minTime)
			{
				minTime = nextTime;
			}
			else
			{
				break;
			}
		}
		fprintf(fOut, "Case #%d: %.7lf\n", iCase++, minTime);
	}
}