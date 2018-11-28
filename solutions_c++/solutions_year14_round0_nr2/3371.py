#include <iostream>
#include <cstdio>
 
using namespace std;

int main() {
	int T, k=0;
	double C, X, F, start=2.0, current_cokiee;
	bool found;
	double sum = 0.0, t1, t2, t3;
	cin >> T;
	while(T--) {
		sum = 0.0;
		start = 2.0;
		cin >> C >> F >> X;
		found = false;
		while(!found) {
			t1 = C/start;
			t2 = X/start;
			t3 = t1 + X/(start+F);
			if(t2<= t3) {
				found = true;
				sum += t2;
				break;
			}
			start += F;
			sum += t1;
		}
		printf("Case #%d: %.7lf\n", ++k, sum);
	}
	return 0;
}