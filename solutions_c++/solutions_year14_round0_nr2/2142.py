#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>

using namespace std;

const double eps=1e-12;

int main() {
	int cases;
	scanf("%d",&cases);
	for (int o=0; o<cases; ++o) {
		double x,y,z,t=0;
		int n=0;
		scanf("%lf%lf%lf",&x,&y,&z);
		while (true) {
			if (z<x+eps||z/(y*n+2.)<x/(y*n+2.)+z/(y*n+y+2.)-eps) {
				t+=z/(y*n+2.);
				break;
			}
			t+=x/(y*n+2.);
			++n;
		}
		printf("Case #%d: %.7f\n",o+1,t);
	}
	return 0;
}

