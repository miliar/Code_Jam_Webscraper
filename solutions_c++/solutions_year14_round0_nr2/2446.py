#include <iostream>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <math.h>
#include <stack>
#include <queue>
#include <list>
#include <limits.h>
#include <time.h>
#include <iterator>

#pragma comment(linker, "/STACK:167772160")

using namespace std;

double C, F, X;
double ans = 1e+18;
double cnt(double _X, double _F) {
	return _X / _F;
}
double f(double currCookie, double currF, double currTime) {
	if(currTime > ans) return currTime;
	double timeToEnd = (X - currCookie) / currF;
	double timeToGo  = (C - currCookie) / currF;

	if(cnt(X, currF + F) + timeToGo > timeToEnd) return ans = min(ans, timeToEnd + currTime);
	return ans = min(ans, min( timeToEnd + currTime, 
		             timeToGo  + f(abs((currCookie + timeToGo * currF) - C ), currF + F, currTime + timeToGo)));
}
int main(){
//	ifstream cin("B-large.in");
//	ofstream cout ("out.txt");
	cout.precision(7);
	int T;
	cin >> T;
	for(int t=1; t<=T; t++){
		cin >> C >> F >> X;
		ans = 1e+18;
		ans = f(0, 2, 0);
		cout << "Case #" << t << ": ";
		cout << fixed << ans << endl;
	}
    return 0;
}