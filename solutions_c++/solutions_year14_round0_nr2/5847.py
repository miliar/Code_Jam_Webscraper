#include <bits/stdc++.h>
using namespace std;
int main() {
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int t; cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase) {
		double profit, incr, limit;
		cin >> profit >> incr >> limit;
		double div = 2;
		double ff = limit / div, ss;
		double prev = 0;
		while(1) {
			ss = prev + profit / div + limit / (div + incr);
			if(ff <= ss) break;
			prev += profit / div;
			div += incr;
			ff = ss;
		}
		printf("Case #%d: %.7lf\n",testCase,ff);
	}
}
