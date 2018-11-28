#include <iostream>
#include <stdio.h>
#include <vector>

#define pb push_back

using namespace std;

double c, f, x;
vector< double > vec;

void read() {
	cin >> c >> f >> x;
}

void solve() {
	vec.clear();
	
	vec.pb(0.0);
	double minT = x / 2.0;
	
	for(int i = 1; ; i ++) {
		double toAdd = vec.back() + c / (2.0 + f * (double)(i - 1));
		vec.pb(toAdd);
		double curT = vec.back() + x / (2.0 + f * (double)i);
		if(curT > minT) break;
		minT = curT;
	}
	
	cout.precision(8);
	cout << fixed << minT << endl;
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; i ++) {
		printf("Case #%d: ", i);
		
		read();
		solve();
	}

    return 0;
}
