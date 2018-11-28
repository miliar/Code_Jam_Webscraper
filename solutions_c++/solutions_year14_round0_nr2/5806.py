#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;


int main(){
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t;
	cin >> t;
	for (int c = 1; c <= t; c++){
		double C, F, X;
		cin >> C >> F >> X;
		double cps = 2.0;
		double bestSoFar = X / cps;
		double total = 0.0;
		while (true){
			double getNewF = C / cps;
			cps += F;
			double getX = X / cps;
			if (total + getNewF + getX > bestSoFar){
				break;
			}
			bestSoFar = total + getNewF + getX;
			total += getNewF;
		}

		printf("Case #%d: %0.7f\n", c, bestSoFar);

	}
	return 0;
}