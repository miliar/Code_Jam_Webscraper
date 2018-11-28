#include <cstdio>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
using namespace std;
#define INF 2000000000
#define INFLL (1LL<<62)
#define SS ({int x;scanf("%d", &x);x;})
#define SSL ({lint x;scanf("%lld", &x);x;})
#define rep(i,n) for(int i=0;i<(n);i++)
#define rept(i,m,n) for(int i=(m);i<(n);i++)
#define ull unsigned long long
#define lint long long
#define MX 10000001

int main() {
	
	int t;
	double C,F,X;
	t=SS;	
	
	for (int testnum=1; testnum<=t; testnum++) {		
		
		cin>>C>>F>>X;
		
		double numFarms = 0.0;
		double timeTaken = 0.0;

		while (timeTaken<X*0.5) {

			//Option1 : Buy a farm with next C cookies
			double timetoBuyFarm = C/(numFarms*F + 2.0);
			double timeWithFarm = X/((numFarms+1)*F + 2.0);

			//Option2 : Collect all cookies to reach X
			double timeWithoutFarm = X/(numFarms*F + 2.0);

			//Select the better choice greedily
			if (timetoBuyFarm + timeWithFarm <= timeWithoutFarm) {
				timeTaken += timetoBuyFarm;
				numFarms += 1.0;
			} else {
				timeTaken += timeWithoutFarm;
				break;
			}

		}

		if(timeTaken > X*0.5) {
			timeTaken = X*0.5;
		}
		printf("Case #%d: %.7f\n",testnum, timeTaken);

	}
	return 0;
}

