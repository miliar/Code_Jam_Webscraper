/*
 * main.cpp
 *
 *  Created on: 2014. 4. 12.
 *      Author: Administrator
 */
#include <stdio.h>

int main()
{
	int testNumber;
	double c, f, x, notBuyingFarmTime, BuyingFarmTime, accumulatedTime, buyingOnefarmTime;
	double cookiesPerSecond = 2.0;

	scanf("%d", &testNumber);
	for (int n = 1; n <= testNumber; n++)
	{
		scanf("%lf", &c);
		scanf("%lf", &f);
		scanf("%lf", &x);
		accumulatedTime = 0.0;
		cookiesPerSecond = 2.0;

		if (x <= c)
		{
			accumulatedTime = x/cookiesPerSecond;
		}
		else
		{
			while (true)
			{
				buyingOnefarmTime = c/cookiesPerSecond;
				notBuyingFarmTime = (x - c)/(cookiesPerSecond);
				BuyingFarmTime = x / (cookiesPerSecond + f);

				accumulatedTime += buyingOnefarmTime;

				if (notBuyingFarmTime <= BuyingFarmTime)
				{
					accumulatedTime += notBuyingFarmTime;
					break;
				}
				else
				{
					cookiesPerSecond +=f;
				}
			}
		}
		printf("Case #%d: %.7lf\n", n, accumulatedTime);
	}

	return 0;
}
