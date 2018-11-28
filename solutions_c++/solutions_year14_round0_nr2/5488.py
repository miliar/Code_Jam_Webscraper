#include<stdio.h>
#include<iostream>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#define print(Z,a,b) for (int __z = a; __z < b; __z ++) cout << Z[__z] << " ";
#define scan(Z,a,b) for (int __z = a; __z < b; __z ++) cin >> Z[__z];
#define bit(_z) (1ll << _z)
using namespace std;

int t;
double C, F, X;

double solve() {
	double ans = X / 2.0;
	
	double farms = 0.0;
	double farm_time = 0.0;
	while ((farms+1.0) * C <= X) {
		farm_time += C / (2.0 + F * farms);
		farms += 1.0;
		
		//ans = min(ans, farm_time + X / (2.0 + F * farms));
		double opt = farm_time + X / (2.0 + F * farms);
		if (ans > opt)
			ans = opt;
	}
	
	return ans;	
}

int main () {
	cin >> t;
	
	int caze = 0;
	while (t --) {
		++ caze;
		cin >> C >> F >> X;
		
		printf("Case #%d: %0.7lf\n", caze, solve());
	}
	
	return 0;
}  	
