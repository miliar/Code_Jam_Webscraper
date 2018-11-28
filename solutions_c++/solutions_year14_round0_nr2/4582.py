#include <iostream>
#include <vector>
#include <cstdlib>
#include <queue>
#include <unordered_set>
#include <algorithm>
#include <map>
#include <sstream>
#include <list>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <set>
#include <utility>


using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int caseid = 1; caseid <= cases; caseid++) {
		double C, F, X;
		cin >> C >> F >> X;
		double time = 0;
		double rate = 2;
		double mintime = X / rate;
		for (int i = 1; time < mintime; i++) {
			time += C/ rate;
			rate += F;
			double t = time + X/rate;
			if (t >= mintime) {
				break;
			}
			mintime = t;
		}
		printf("Case #%d: %.7f\n", caseid, mintime);
	}
	return 0;
}
