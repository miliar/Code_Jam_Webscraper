#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	double c,f,x;
	cin>>T;
	for(int k=1; k<=T; k++) {
		cin>>c>>f>>x;
		double v=2,t=0;
		while(1){
			if (t+x/v < t+c/v+x/(v+f)) {
				printf("Case #%d: %.7lf\n", k, t+x/v);
				break;
			} else {
				t+=c/v;
				v+=f;	
			}
		}
	}
	return 0;
}