#include<iostream>
#include<vector>
#include<cfloat>
#include<cstdio>
#include<algorithm>

using namespace std;

int main(){
	int tests;

	cin >> tests;

	for(int test = 1; test <= tests; ++test){
		int n;
		double goal, tmp;

		cin >> n >> goal >> tmp;
		
		vector<double> tmps(n, 0);
		vector<double> speed(n, 0);


		double mx = -1024, mn = 1024;
		for(int i = 0; i < n; ++i){
			cin >> speed[i] >> tmps[i];

			mx = max(tmps[i], mx);
			mn = min(tmps[i], mn);
		}

		printf("Case #%d: ", test);

		if(mx < tmp || mn > tmp){
			printf("IMPOSSIBLE\n");
			continue;
		}

		double ans = 1e100;
		double lowtmp = 0;
		double lowspeed = 0;
		double hightmp = 0;
		double highspeed = 0;
		double eqspeed = 0;
		for(int i = 0; i < n; ++i){
			if(tmps[i] == tmp){
				eqspeed += speed[i];
			}else if(tmps[i] < tmp){
				lowspeed += speed[i];
				lowtmp += speed[i] * tmps[i];
			}else{
				highspeed += speed[i];
				hightmp += speed[i] * tmps[i];
			}
		}

		hightmp /= highspeed;
		lowtmp /= lowspeed;

		double lows = 1;
		double his = (lowtmp - tmp) / (tmp - hightmp);
		double s = lows + his;
		lows /= s;
		his /= s;

		if(lowspeed == 0 || highspeed == 0){
			printf("%.16f\n", goal/eqspeed);
			continue;
		}

		ans = max(goal * lows / lowspeed, goal * his / highspeed);

		printf("%.16f\n", ans);
	}

	return 0;
}
