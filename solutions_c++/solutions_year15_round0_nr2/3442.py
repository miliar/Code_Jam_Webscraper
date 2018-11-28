#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

#define foreach(it, s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)

const int N = 100001;
const int MOD = 1e9 + 7.5;

int calc(vector<int> &v, int val) {
    int ret = 0;
    foreach(it, v) if (*it > val) {
        ret += (*it / val + (*it % val != 0)) - 1;
    }
    return ret;
}

int solve() {
    int n, val;
    priority_queue<int> q;
    cin >> n;
    vector<int> v;
    for (int i = 0; i < n; i++) {
        cin >> val;
        v.push_back(val);
    }

    int ret = 0x3f3f3f3f;
    for (int i = 1; i <= 1000; i++) {
        ret = min(ret, calc(v, i) + i);
    }

    return ret;
}

int main(){
    freopen("./B-large.in", "r", stdin);
    freopen("bl.out", "w", stdout);
    int ca;
    cin >> ca;
    for (int i = 0; i < ca; i++) {
        printf("Case #%d: %d\n", i + 1, solve());
    }
    return 0;
}
