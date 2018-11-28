#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <iomanip>
#include <locale>
#include <sstream>
#include <vector>
using namespace std;

double c, f, x;
int it, T;

int main() {
	scanf("%d", &T);
	for (int it = 1; it <= T; it++) {
		scanf("%lf %lf %lf", &c, &f, &x);
		c /= 2;  f /= 2;  x /= 2;
		double ret = 1e18;
		double base = 0;
		for (int farm = 0; ; farm++) {
			if (base >= ret) break;
			ret = min(ret, base + x/(1.0 + f * farm));
			base += c/(1 + f * farm);
		}
		printf("Case #%d: %.18lf\n", it, ret);
	}
}