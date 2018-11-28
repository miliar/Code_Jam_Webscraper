#include <sstream>
#include <iostream>
#include <set>
#include <stdio.h>
using namespace std;

int main() {
	freopen("B-large (1).in", "r", stdin);
	freopen("B.out", "w", stdout);

	int T;
	cin>>T;
	for(int caseNumber=1;caseNumber<=T;caseNumber++) {
		double c,f,x;
		cin>>c>>f>>x;
		double v=2;
		double time=0;
		while(c*v+c*f-x*f<0){
			time+=c/v;
			v=v+f;
		}

		printf("Case #%d: ", caseNumber);
		printf("%e\n",x/v+time);
	}
	return 0;
}

