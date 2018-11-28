#include <iostream>;
#include <stdio.h>
#include <string>
#include <limits>


using namespace std;

double kTime[10000];
double sum[10000];
double totalTime[10000];
double G = 2.0;
double C,F,X;

//计算购买第K台机器的时间
double getTimeBuyKMachine(int k)
{
	kTime[k] = (C * k + sum[k-1] * F ) / (G + (k - 1) * F);
	sum[k] = sum[k-1] + kTime[k];
	return kTime[k];
}

//计算在拥有K台机器下，达到目标的时间
double getTimeByKMachine(int k)
{
	totalTime[k] = (X + k * C + F * sum[k]) / (G + k * F);
	return totalTime[k];
}

int main()
{
	kTime[0] = 0;
	sum[0] = 0;

	int T;
	scanf("%d", &T);
	for(int index = 1; index <= T; index++)
	{

		scanf("%lf %lf %lf", &C,&F,&X);
		int minK = 0;
		totalTime[0] = X / G;

		int maxCount = (int)X;
		for(int i = 1; i <= maxCount; i++)
		{
			getTimeBuyKMachine(i);
			getTimeByKMachine(i);
			if(totalTime[i] < totalTime[minK])
				minK = i;
		}

		printf("Case #%d: %.7f\n", index, totalTime[minK]);
	}

	//system("pause");
	return 0;
}

