#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

double mini;

double nextFarm(double perSecond, double c) {
	return c / perSecond;
}

double finished(double perSecond, double x) {
	return x / perSecond;
}

double getAns(double perSecond, double t, double c, double f, double x) {
	double fin = finished(perSecond, x);
	double farm = nextFarm(perSecond, c);
	
	if (t + farm >= mini) {
		return min(mini, t + fin);
	} else {
		mini = min(mini, t + fin);
		return min(mini, t + farm + getAns(perSecond + f, t + farm, c, f, x));
	}
	
	return 1000000000;
}

void solve() {
	double c, f, x;
	
	cin >> c >> f >> x;
	mini = 1000000000;
	printf("%.7lf", getAns(2.0, 0.0,  c, f, x));
}

int main() {
	int cases;
	int i = 1;
	
	cin >> cases;
	while (cases--) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
		i++;
	}
	
	return 0;
}