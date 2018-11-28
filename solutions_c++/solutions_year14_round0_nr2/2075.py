#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

static int cc = 1;
void output() {
	printf("Case #%d: ", cc++);
}
void readfile(const char* a) {
	freopen(a, "r", stdin);
	freopen("res", "w", stdout);
}
//#define __READFIEL__;
int main() {
	int cas;
	#ifdef __READFIEL__
	readfile("B--large.in");
	#endif
	cin>>cas;
	double c, x, f;
	double cost;
	double aim_t,cost_t;
	double sum;
	while(cas--) {
		cin>>c>>f>>x;
		output();
		if(c >= x) {
			printf("%.7f\n",x / 2);
		}
		else {
			sum = 0;
			cost = 2;
			while(true) {
				sum += c / cost;
				aim_t = (x - c) / cost;
				cost_t = x / (cost + f);
				if(aim_t > cost_t) {
					cost += f;
				}
				else {
					sum += aim_t;
					break;
				}
			}
			printf("%.7f\n", sum);
		}
	}
}