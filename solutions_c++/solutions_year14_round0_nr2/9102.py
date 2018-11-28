#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdlib>

using namespace std;

#define SI ({int __; scanf("%d", &__); __;})

int main() {
	int TC = SI;
	for(int tc = 1;tc <= TC;++tc) {
		printf("Case #%d: ", tc);
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		double mini = x/2.00, speed = 2.00, prev = 0.0;
		for(int i = 1;i < 500111;++i) {
			prev += c/speed;
			speed += f;
			double time = prev + x/speed;
			if(time < mini) {
				mini = time;
			} 
		}
		printf("%.7lf\n", mini);
	}		
}
