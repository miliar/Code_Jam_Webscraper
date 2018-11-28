/*
 * cookie.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: prakhar
 */
#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <stdio.h>
#include <vector>
int main(int a, char** v)
{
	int numCases;
	scanf("%d",&numCases);
	int i;
	for (i = 0; i < numCases; ++i) {
		double c,f,x,cookies = 0.0;
		scanf("%lf %lf %lf",&c,&f,&x);
		double time = 0.0;double inc = 2.0;
		while(1)
		{
			if(c < x)
			{
				double timectox = (x-c)/inc;
				double recovertimec= c/f;
				if(recovertimec < timectox)
				{
					time += c/inc;
					inc += f;
					continue;
				}
				else
				{
					time += x/inc;
					break;
				}

			}
			else
			{
				time += x / inc;
				break;
			}
		}
		printf("Case #%d: %.7f\n",i+1,time);
	}

	return 0;
}
