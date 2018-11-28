#include <cstdio>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <set>
#include <cassert>
#include <map>
#define INF 0x3f3f3f3f
#define mem(a, b) memset((a), (b), sizeof(a))

using namespace std;

const double eps = 1e-8;
const long long mod = 998244353ll;
const long long _3 =   333333336ll;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

long long fpow(long long a, long long b) {
    long long ret = 1;
    while(b) {
        if(b % 2 == 1) {
            ret *= a;
            ret %= mod;
        }
        a = a * a;
        a %= mod;
        b /= 2;
    }
    return ret;
}

char cread;
inline void read(int &x) {
    while((cread=getchar())<'0') {}
    x = cread - '0';
    while((cread=getchar())>='0') x = x * 10 + cread - '0';
}

double sqr(double a) {
    return a * a;
}

const double pi = acos(-1.0);

int n;
double v[19], x[19];

int MAIN() {
	scanf("%d", &n);
	for(int i = 0; i <= n; i++) {
		scanf("%lf%lf", &v[i], &x[i]);
	}
	if(n == 1) {
		if(fabs(x[1] - x[0]) < eps) {
			printf("%.9f\n", v[0] / v[1]);
		} else {
			printf("IMPOSSIBLE\n");
		}
	} else {
		if(fabs(x[1] - x[0]) < eps && fabs(x[2] - x[0]) < eps) {
			printf("%.9f\n", v[0] / (v[1] + v[2]));
		} else if(fabs(x[1] - x[0]) < eps) {
			printf("%.9f\n", v[0] / v[1]);
		} else if(fabs(x[2] - x[0]) < eps) {
			printf("%.9f\n", v[0] / v[2]);
		} else if(!((x[1] > x[0]) ^ (x[2] > x[0]))) {
			printf("IMPOSSIBLE\n");
		} else {
				swap(x[1], x[2]);
				swap(v[1], v[2]);
				x[1] -= x[0];
				x[2] -= x[0];
				x[1] = fabs(x[1]);
				x[2] = fabs(x[2]);
				double t1 = v[0] * (x[2] / (x[1] + x[2])) / v[1];
				double t2 = v[0] * (x[1] / (x[1] + x[2])) / v[2];
				printf("%.9f\n", max(t1, t2));
		}
	}
    return 0;
}

int main() {
    int cases;
    scanf("%d", &cases);
    int cc = 1;
    
    
    while(cases--) {
    //while(~scanf("%d", &n)) {
    	printf("Case #%d: ", cc++);    
        MAIN();
    }
    return 0;
}
