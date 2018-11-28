#include <cstdio>
#include <cstring>
#include <list>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

#define foreach(it, s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)
#define X first
#define Y second

const int MAX_N = 100001;
const int MAX_M = 100001;
const int MOD = 1e9 + 7.5;
const double EPS = 1e-8;
const int INF = 0x3f3f3f3f;

int n;
list<int> lst;

void init() {
    lst.clear();
    cin >> n;
    int val;
    for (int i = 0; i < n; i++) {
        cin >> val;
        lst.push_back(val);
    }
}

void solve(int ca) {
    int ret = 0;
    __typeof(lst.begin()) iter;
    for (int i = 0; i < n; i++) {
        int minval = INF, pos;
        int cnt = 0;
        for (__typeof(lst.begin()) it = lst.begin(); it != lst.end(); ++it) {
            if (*it < minval) {
                minval = *it;
                pos = cnt;
                iter = it;
            }
            ++cnt;
        }
        ret += min(pos, (int)(lst.size() - pos - 1));
        lst.erase(iter);
    }
    printf("Case #%d: %d\n", ca, ret);
}

int main(){
    freopen("a1.in", "r", stdin);
    freopen("a1.out", "w", stdout);
    int ca;
    cin >> ca;
    for (int i = 0; i < ca; i++) {
        init();
        solve(i + 1);
    }
    return 0;
}
