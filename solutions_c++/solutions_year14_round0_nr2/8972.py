#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <string>
#include <cfloat>

#define ForT for(int t=1;t<=T;t++)
#define REP(x,s,n) for(int x=s; x<n; x++)
#define EPSILON (1.0E-6)
using namespace std;

typedef long long LL;
typedef double LD;
LD CompareDouble(LD , LD);
LD solve(LD, LD, LD);

int main() {
    int T;
    freopen("2B.in", "r+", stdin);
    freopen("2B.txt", "w+", stdout);
    cin >> T;
    ForT {
	LD C, F, X;
        cin >> C >> F >> X;
        LD ans = solve(C, F, X);
        printf("Case #%d: %0.7lf\n", t, ans);
    }
    return 0;
}

LD solve(LD C, LD F, LD X) {
    LD a = 2.0;
    if (C >= X) return X/a;
    LD minsum = X/a;
    LD csum = C/a;
    int i = 1;
    while(1) {
        LD cursum = (csum + X/(a+i*F));
	if (cursum >= minsum) {
            break;
        }
        else {
            minsum = cursum;
        }
	csum = csum + C/(a+i*F);
        i++;
    }
    return minsum;
}

LD CompareDouble(LD a, LD b) {
    return fabs(a - b) < EPSILON;
}
