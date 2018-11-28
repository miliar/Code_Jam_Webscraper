//
//  main.cpp
//  CookieClicker
//
//  Created by 김민규 on 4/12/14.
//  Copyright (c) 2014 Micky. All rights reserved.
//

#define MAX_CASE 100
#define BASIC_COOKIE 2.0

#include <iostream>
using namespace std;
int main(int argc, const char * argv[])
{
	char result[MAX_CASE][30];
	int a, t_c;
	
	
	cin >> t_c;
	for (a=0; a<t_c; a++) {
		double f_cost;
		double f_rate;
		double goals;
		double time = 0.0, next_time = 0.0;
		//double curr_cookie = 0;
		//double f_cnt = 0.0;
		cin >> f_cost >> f_rate >> goals;
		
		for (int i=0;true;i++) {
			double farm_time[2] = {0,};
			if(i) {
				for(int j=0;j<i;j++) {
					farm_time[0] += 1/(BASIC_COOKIE+j*f_rate);
				}
				farm_time[0] *= f_cost;
				farm_time[1] = farm_time[0] + f_cost/(BASIC_COOKIE+i*f_rate);
			}
			else {
				farm_time[0] = 0;
				farm_time[1] = f_cost/BASIC_COOKIE;
			}
			
			time = farm_time[0]+goals/(BASIC_COOKIE+i*f_rate);
			next_time = farm_time[1]+goals/(BASIC_COOKIE+(i+1)*f_rate);
			
			//cout << endl << time << next_time << endl;
			
			if(time < next_time) break;
		}
		
		sprintf(result[a], "Case #%d: %lf\n", a+1, time);
	}
	
	for (int i = 0; i<t_c; i++) {
		cout << result[i];
	}
	
    return 0;
}

