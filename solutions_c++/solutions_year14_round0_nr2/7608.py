#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int testCases;
	
	
	scanf("%d", &testCases);
	for(int i = 1; i<=testCases; i++)
	{
		bool flag = 0;
		double totalTime = 0.0;
		double C, F, X;
		double restTime = 0.0;
		double nextTime = 0.0;
		double coockieRate = 2.0;
		cin>>C>>F>>X;
		restTime = X/coockieRate;
		nextTime = (C/coockieRate)+(X/(coockieRate+F));
		
		while(restTime > nextTime){
			totalTime += (C/coockieRate);
			coockieRate += F;
			restTime = X/coockieRate;
			nextTime = (C/coockieRate)+(X/(coockieRate+F));
			flag = 1;
		}
		if(flag == 1)
			totalTime += (X/coockieRate);
		else
			totalTime = restTime;
		printf("Case #%d: %.7f\n",i,totalTime);
	}
	return 0;
}
