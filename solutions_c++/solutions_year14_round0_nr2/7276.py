#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#define pb push_back
#define mp make_pair
#define REP(i, N) for(int i = 0; i < (N); i++)
#define eps 10e-9
using namespace std;

int main() {
	int T, testcase=1;
	scanf("%d", &T);
	while(T--) {
		long double C, F, X;
		scanf("%Lf%Lf%Lf", &C, &F, &X);
		long double cPerSec = 2.0;
		long double ans = X/cPerSec; 
		bool cont = true;
		long double farms = 0;
		while(cont) {
			cont = false;
			long double nans = farms+C/cPerSec;
			farms += C/cPerSec;
			cPerSec += F;
			nans += X/cPerSec;
			if(nans+eps < ans) {
				cont = true;
				ans = nans;
			}
		}

		printf("Case #%d: ", testcase++);
		printf("%.7Lf", ans);
		printf("\n");
	}
	
	return 0;
}
