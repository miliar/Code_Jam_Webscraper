//
//  main.cpp
//  EleProInter
//
//  Created by lhdgriver on 14-4-3.
//  Copyright (c) 2014年 lhdgriver. All rights reserved.
//

#include<stdio.h>
#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	int t;
	cin>>T;
	for(t = 1;t <= T;t ++)
	{
		double C,F,X;
		cin>>C>>F>>X;
		double rate = 2.0;
		double time = 0.0;
		double now = 0.0;
		double remain = 0.0;
		double farm = 0.0;
		while(true)
		{
			remain = (X - now) / rate;
			farm = (C - now) / rate + X / (rate + F);
			if(remain < farm)
			{
				time += remain;
				break;
			}
			else
			{
				time += (C - now) / rate;
				rate += F;
			}
		}
		cout<<"Case #"<<t<<": "<<fixed<<setprecision(7)<<time<<endl;
	}
	fclose(stdin);
	fclose(stdout);
}