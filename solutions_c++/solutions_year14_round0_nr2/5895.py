#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cstring>
#include <sstream>
using namespace std;
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; tc++) {
		double res = 0;
		double c, f, x, rate = 2.0;
		cin >> c >> f >> x;
		while(true) {
			if(( c*1.0 / rate ) + ( x*1.0 / ( rate + f ) ) >= ( x*1.0 / rate )) break;
			res += ( c*1.0 / rate );
			rate += f;
		}
		res += ( x*1.0 / rate );
		cout.precision(7);
		cout << "Case #" << tc << ": " << fixed << res << endl;
	}
	return 0;
}
