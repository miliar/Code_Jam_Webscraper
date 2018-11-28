#include <cstdio>
#include <iostream>
#include <queue>
#include <algorithm>
#include <cmath>
using namespace std;

double C,F,X;

int main(){
	int T;
	int iCase = 0;
	cin >> T;
	while(cin >> C >> F >> X){
		if( X <= C ){
			printf("Case #%d: %.8lf\n",++iCase,X/2.0);
			continue;
		}
		double tMin = X/2.0;

		double ts = 0.0;
		double v = 2.0;
		for(int k=1;k<=10000;++k){
			ts += C/v;
			v = v + F;
			if( ts + X/v < tMin )
				tMin = ts + X/v;
			else{
				break;
			}
		}
		printf("Case #%d: %.8lf\n",++iCase,tMin);
	}
	return 0;
}
