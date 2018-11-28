#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
#include <string>

using namespace std;

typedef long long ll;

int test;
ll r, t;

ll calc(ll k) {
    return k*(1+2*r+2*(k-1));
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("bullseye.out", "w", stdout);
    
    scanf("%d", &test);
    for(int ttest = 1; ttest <= test; ttest++) {
        scanf("%lld%lld", &r, &t);
        ll left = 0, right = min(1000000000LL, t/r);
        while (left+1 < right) {
            ll mid = (left+right)/2;
            if (calc(mid) <= t) left = mid;
            else right = mid;
        }
        if (calc(right) <= t) left = right;
        printf("Case #%d: %lld\n", ttest, left);
    }
    
	return 0;
}
