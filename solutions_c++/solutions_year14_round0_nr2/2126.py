#include<iostream>
#include<stdio.h>
#include<cstring>
#include<stdlib.h>
#include <queue>
#include<string>
#include <sstream>
#include<list>
#include<map>
#include<cmath>
#include<algorithm>
#include <unordered_map>
using namespace std;
#define INF 1e9
#define DIVIDE 10000
//Cookie Clicker_Alpha GCJ2014 B
int main()
{
	int	flag = 0,answer,n,i=0,j,index = 0;
	freopen ("d:/Codejam/B-large.in","r",stdin);
    freopen ("d:/Codejam/B-large.out","w",stdout);
	scanf("%d",&n);
	double C,F,X,time,rate,req_time,req_time_extra_farm,a;
	//bool b_ex[1005],c_ex[1005];
	while(n--)
	{
		rate=2.0;
		scanf("%lf %lf %lf",&C,&F,&X);

		time=0.0;
        
        req_time = X/2;

        req_time_extra_farm=( X/ (F+2)) + C/2;

        while(true)
        {
			if (req_time_extra_farm < req_time)
			{
            req_time = req_time_extra_farm;
            time = time + (C / rate);
            rate = rate + F;
            req_time_extra_farm = time + (C / rate);
			a =(X / (rate + F));
			req_time_extra_farm = req_time_extra_farm + a;
			}
			else
				break;

        }
			printf("Case #%d: ",++index);
			printf("%.7lf\n",  req_time);
	}
	return 0;
}
