#include <iostream>
#include <stdio.h>
#include <math.h>
#include <list>
#include <queue>
#include <vector>
#include <functional>
#include <stack>
#include <utility> 
#include <stdlib.h>
#include <map>
#include <string.h>
#include <algorithm>
typedef long long int ll;
#define SWAP(a, b) (((a) ^= (b)), ((b) ^= (a)), ((a) ^= (b)))
#define gc getchar_unlocked
#define CLR(a) memset(a, 0, sizeof(a))
using namespace std;
int main() {
	int t, i, j, k;
	double c, f, x, rate, totaltime, trate, ttime, ttime1, ttime2;
	cin>>t;
	for(k=1;k<=t;++k) {
		rate = 2.0;
		totaltime = 0.0;
		cin>>c>>f>>x;
		while(1) {
			ttime = x/rate;
			ttime1 = c/rate;
			trate = rate + f;
			ttime2 = ttime1 + x/trate;
			if(ttime < ttime2) {
				totaltime += ttime;
				break;
			} else {
				totaltime += ttime1;
				
				rate = trate;
			}
		}
		printf("Case #%d: %.7f\n", k, totaltime);
	}
	return 0;
}
