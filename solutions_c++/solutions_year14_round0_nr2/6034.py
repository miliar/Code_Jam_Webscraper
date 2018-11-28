#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<cstdio>

using namespace std;

double calc (double cost, double farm, double x){ // x is goal
	double ret = 1e15;
	//한 상태는 현재 상태의 cps, cookie, 걸린 시간 으로 표시된다.
	double curCps = 2.0, curTime = 0;
	int steps = 1000000;
	while(steps--){
		//try x
		ret = std::min(curTime + x/curCps, ret);
		
		//if(ret < curTime + x/curCps) return ret;
		
		//go to next state
		curTime += cost/curCps;
		curCps += farm;
	}
	
	return ret;
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("output_b_large.txt", "w", stdout);
	
	int fullCase;
	cin >> fullCase;
	for(int tc = 1; tc <= fullCase; ++tc){
		double c, f, x;
		cin >> c >> f >> x;
		printf("Case #%d: %.7lf\n", tc, calc(c, f, x));
	}
	return 0;
}
