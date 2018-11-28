/*
 * cookieClick.cpp
 *
 *  Created on: Apr 11, 2014
 *      Author: kamalsharma
 */

#include <stdio.h>

using namespace std;

void calculateCookieTime(double c, double f, double x, double genRate, double time, double *minTime)
{
	double t1 = time + x/genRate;
	if(t1<*minTime)
		*minTime = t1;

	double timeForFarm = time + c/genRate;
	if(timeForFarm>*minTime)
		return;

	calculateCookieTime(c,f,x,genRate+f, timeForFarm, minTime);
}

int main()
{
	int noTests = 0, caseNo = 0;
	float c,f,x;
	double minTime;

	scanf("%d\n",&noTests);
	for(int i=0, caseNo=1; i<noTests; i++, caseNo++)
	{
		scanf("%f %f %f\n", &c, &f, &x);
		minTime = x/2;
		calculateCookieTime(c,f,x,2,0,&minTime);
		printf("Case #%d: %.7f\n", caseNo, minTime);
	}
}
