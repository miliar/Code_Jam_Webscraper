#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <queue>
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
#include <cstring>
#include <ctime>

using namespace std;

const int modulo = 1000002013;

struct item {
    int loc, cnt, type;
    item(int loc = 0, int cnt = 0, int type = 0) {
        this->loc = loc;
        this->cnt = cnt;
        this->type = type;
    }
    bool operator < (const item &o) const {
        return loc < o.loc || loc == o.loc && type < o.type;
    }
};

item bracket[2000];
item s[2000];

int calc(int n, int k) {
    return (long long)k * (2 * n + 1 - k) / 2 % modulo;
}

void work() {
    int n, m;
    scanf("%d%d", &n, &m);
    long long ans = 0;
    for (int i = 0; i < m; i ++) {
        int o, e, p;
        scanf("%d%d%d", &o, &e, &p);
        bracket[i * 2] = item(o, p, 0);
        bracket[i * 2 + 1] = item(e, p, 1);
        ans = (ans + (long long)calc(n, e - o) * p) % modulo;
    }
    sort(bracket, bracket + m * 2);
    int top = 0;
    for (int i = 0; i < m * 2; i ++) {
        if (bracket[i].type == 1) {
            int t = bracket[i].cnt;
            while (true) {
                if (s[top - 1].cnt > t) {
                    s[top - 1].cnt -= t;
                    ans = (ans - (long long)calc(n, bracket[i].loc - s[top - 1].loc) * t) % modulo;
                    break;
                } else {
                    ans = (ans - (long long)calc(n, bracket[i].loc - s[top - 1].loc) * s[top - 1].cnt) % modulo;
                    t -= s[top - 1].cnt;
                    top --;
                }
            }
        } else {
            s[top ++] = bracket[i];
        }
    }
    ans = (ans + modulo) % modulo;
    printf("%lld\n", ans);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test ++) {
        printf("Case #%d: ", test + 1);
        work();
    }

    return 0;
}