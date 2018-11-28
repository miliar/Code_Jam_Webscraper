#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <complex>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)
#define ALL(x) (x).begin(),(x).end()
#define LL long long

using namespace std;

double getSeconds(double produce, double cookies){
	return cookies / produce;
}

int main(){
	int T;
	cin >> T;
	REP(testCase, T){
		double C, F, X;
		cin >> C >> F >> X;
		
		double produce = 2.0;
		double seconds = 0.0;
		double bestSec = getSeconds(produce, X);
		while (seconds<=bestSec){
			double secForGoal = getSeconds(produce, X);
			bestSec = min(bestSec, seconds + secForGoal);
			seconds += getSeconds(produce, C);
			produce += F;
		}
		printf("Case #%d: %.7f\n", testCase + 1, bestSec);
	}
	return 0;
}