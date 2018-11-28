#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int t;
	double c, f, x;
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &t);
	
	for(int cs = 1; cs <= t; ++cs) {
		scanf("%lf%lf%lf", &c, &f, &x);
		
		double current_cookies = 0.0;
		double current_production = 2.0;
		double time = 0.0;
		
		while(current_cookies < x) {
				if(current_cookies < c) {
					double needed = c - current_cookies;
					double dist = x - current_cookies;
					
					if(dist < needed) {
						time += dist / current_production;
						break;
					} else {
						time += needed / current_production;
						current_cookies = c;
					}
					
					continue;
				}
				
				double dist = x - current_cookies;
								
				double normal_time = dist / current_production;
				double time_if_bought = x / (current_production + f);
				
				if(normal_time > time_if_bought) {
					current_production += f;
					current_cookies = 0;
				} else {
					time += dist / current_production;
					break;
				}
		}
		
		printf("Case #%d: %.8lf\n", cs, time);
	}
	
	return 0;
}
