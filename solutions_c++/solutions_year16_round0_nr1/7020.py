#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long ll;

const int MAX_ITER = 1e5;

int solve(int n) {
    set<int> digits;

    ll cur = n;
    int iter = 0;

    while(iter <= MAX_ITER) {
        ll tmp = cur;
        while(tmp) {
            digits.insert(tmp % 10);
            tmp /= 10;
        }

        if(digits.size() == 10)
            break;
        cur += n;
        ++iter;
    }

    if(digits.size() != 10)
        return -1;
    return cur;
}

int main() {
    int tc;
    scanf("%d", &tc);
    for(int ii=1;ii<=tc;++ii) {
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", ii);

        ll ans = solve(n);
        if(ans == -1)
            printf("INSOMNIA\n");
        else
            printf("%lld\n", ans);
    }
    return 0;
}
