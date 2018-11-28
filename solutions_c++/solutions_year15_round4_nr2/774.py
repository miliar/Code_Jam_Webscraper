#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

double r[111], c[111];

int main() {
	int T;
	cin>>T;
	for(int t=1;t<=T;t++) {
		int n;
		cin>>n;
		double v, x;
		cin>>v>>x;
		for(int i=0;i<n;i++) cin>>r[i]>>c[i];
		if(n==2 && fabs(c[0] - c[1]) < 1e-9) {
			n=1;
			r[0] += r[1];
		}
		if(n==1) {
			if(fabs(c[0] - x) >= 1e-9) {
				cout << "Case #"<<t<<": IMPOSSIBLE"<<endl; 
			}
			else {
				printf("Case #%d: %.12lf\n", t, v/r[0]);
			}
		}
		else if(n==2) {
			double va = v * (x - c[1]) / (c[0] - c[1]);
			double vb = v * (c[0] - x) / (c[0] - c[1]);
			if(va <= -1e-12 || vb <= -1e-12) {
				cout << "Case #"<<t<<": IMPOSSIBLE"<<endl; 
			}
			else {
				printf("Case #%d: %.12lf\n", t, max(va/r[0], vb/r[1]));
			}
		}
		else {
			cout << "Case #"<<t<<": NOT INSIDE LIMITS"<<endl; 
		}
	}
	return 0;
}
