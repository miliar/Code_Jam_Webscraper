#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <vector>
using namespace std;
int main() {
	double c, f, x;
	int _, ca(0); cin>>_;
	while(_--) {
		cin>>c>>f>>x;
		double cur = 2, t = 0;
		while(x/cur > x/(cur+f)+c/cur) {
			t+=c/cur;
			cur+=f;
		}
		printf("Case #%d: %lf\n", ++ca, t+x/cur);
	}
	return 0;
}
