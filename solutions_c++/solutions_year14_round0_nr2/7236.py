#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <stack>
#include <cstring>
#include <vector>
#include <string>
#include <cctype>
#include <iomanip>
#include <map>
#include <sstream>
#include <queue>
#define inf 0x7fffffff
#define MOD 1000000007

using namespace std;

int main() {
	FILE* in = fopen("B-large.in", "r");
	FILE* out = fopen("B-large.out", "w");
	int t;
	fscanf(in, "%d", &t);
	for(int ca = 1; ca <= t; ca++) {
		fprintf(out, "Case #%d: ", ca);
		double c, f, x;
		fscanf(in, "%lf%lf%lf", &c, &f, &x);
		if(c >= x) {
			fprintf(out, "%.7lf\n", x/2);
		}else {
			double res = 0;
			int k = 0;
			for(k=0;; k++) {
				double d = (x-c)/(2+k*f)*(2+(k+1)*f);
				if(d <= x)
					break;
			}
			int j = 0;
			while(j < k) {
				res += c/(2+j*f);
				j++;
			}
			res += x/(2+k*f);
			fprintf(out, "%.7lf\n", res);
		}
	}

	fclose(in);
	fclose(out);

	return 0;
}