#include<iostream>
#include<vector>
#include<cstdio>
#include<set>
#include<map>
#include<algorithm>
#include<string.h>
#include<string>
#include<cassert>
#include<stack>
#include<queue>
#include<cmath>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int, int> PI;

double c, f, x;

/*
 *  limit = max limit in which we are sure to reach the goal.
 */

double solve(double initial, double R, double limit) {
    if(initial > limit) return limit;    

    double ans1 = x/R + initial;
    double ans2 = solve(initial + c/R, R + f, min(ans1, limit));

    return min(ans1, ans2);
}

int main() {
    int t;
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++) {
        scanf("%lf %lf %lf", &c, &f, &x);
        double ans = solve(0.0, 2.0, x/2.0);
        printf("Case #%d: %.7lf\n", tt, ans);
    }
}
