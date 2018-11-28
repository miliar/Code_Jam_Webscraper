#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <cstring>
#include <stack>
#include <queue>

using namespace std;

typedef long long int lli;

int main()
{
	int t;
	double c, f, x;
	double time1, time2;
	double curr_cookies;
	double curr_time;
	double curr_speed;
	int t1 = 1;	
	
	scanf("%d", &t);
	
	while (t--) {
		cin >> c >> f >> x;
		curr_cookies = 0;
		curr_time = 0;
		curr_speed = 2.0;
		
		while (curr_cookies < x ) {
			if (curr_cookies >= c) {
				time1 = (x - curr_cookies) / curr_speed;
				time2 = (x - curr_cookies + c) / (curr_speed + f);
				
				if (time1 < time2) {
					if (x - curr_cookies  > c) {
						curr_cookies = curr_cookies + c;
						curr_time = curr_time + (c / curr_speed);
					}
					else {
						curr_time = curr_time + ((x - curr_cookies) / curr_speed);
						curr_cookies = x;
					}
				}
				else {
					curr_cookies = curr_cookies - c;
					curr_speed = curr_speed + f;
				}
			}
			else {
				if (x - curr_cookies > c) {
					curr_cookies = curr_cookies + c;
					curr_time = curr_time + (c / curr_speed);
				}
				else {
					curr_time = curr_time + ((x - curr_cookies) / curr_speed);
					curr_cookies = x;
				}
			}
		}
		
		printf("Case #""%d",t1);
		printf(": ""%0.7lf\n", curr_time);
		t1++;
	}
	
	return 0;
}	
