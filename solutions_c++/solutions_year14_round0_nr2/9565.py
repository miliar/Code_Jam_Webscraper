#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int count=1; count<=T; count++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		
		double prevTime = (unsigned long)(-1);	// INF
		double time;
		int n;
		for(n=0; n<10000; n++)
		{
			time = 0;
			for(int i=0; i<=n-1; i++)
				time += C/(i*F+2);
			time += X/(n*F+2);
			
			if(time > prevTime)
				break;
				
			prevTime = time;
		}
		printf("Case #%d: %0.7f\n", count, prevTime);
	}
	return 0;
}
