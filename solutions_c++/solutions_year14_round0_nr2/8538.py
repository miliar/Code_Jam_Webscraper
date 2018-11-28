#include <iostream> 
#include <cstdio>
using namespace std;


int main() 
{ 
    freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	cin >> T;
	for(int t = 0; t < T; ++t) 
	{	
		printf("Case #%d: ", t + 1);

		double C,F,X;
		double PT = 0;
		double speed = 2;
		
	
		cin >> C >> F >> X;		
		double time1 = X / speed;

		if( X <= C)
		{
			printf("%.7f",time1);
		}
		else
		{
			while(1)
			{
				PT = PT + C / speed;
				speed = speed + F;
				double time2 = PT + X /speed;
		
				if (time2 >= time1)
				{
					break;
				}
				else
				{
						time1 = time2;
				}
			}
			printf("%.7f", time1);
		}
		
		
		printf("\n");
		}
		//system("pause");
		return 0;

}

