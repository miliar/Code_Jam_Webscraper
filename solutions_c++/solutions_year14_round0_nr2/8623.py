#include <stdio.h>

double price, rate, need, currentrate, cookie, time = 0;

int logicalToAddFarm()
{
	if(((need-cookie) / currentrate)<((need - cookie + price) / (currentrate + rate))) return 0; // do not add
	return 1; // add
}

void addFarm()
{
	currentrate += rate;
	cookie -= price;
}

int main()
{
	int times;
	scanf("%d", &times);
	
	for(int tm = 1; tm <= times; tm++)
	{
		currentrate = 2, cookie = 0, time = 0;
		scanf("%lf %lf %lf", &price, &rate, &need);
		
		if(logicalToAddFarm() == 0)
		{
			printf("Case #%d: %.7lf\n",tm, ((need-cookie) / currentrate));
		}
		
		else
		{
			while(logicalToAddFarm() == 1)
			{
				if(cookie>=price)
				{
					addFarm();
				}
				
				else
				{
					time += ((price-cookie)/currentrate);
					cookie = price;
				}
				
			}
			
			time += ((need-cookie) / currentrate);
			printf("Case #%d: %.7lf\n",tm, time);
		}
		
	}
	
	return 0;
}
