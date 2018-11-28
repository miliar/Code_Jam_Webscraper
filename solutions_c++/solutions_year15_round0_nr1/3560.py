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

int solve() {
    int len;
    string str;
    cin >> len >> str;
    int ret = 0, tot = 0;
    for (int i = 0; i < str.size(); i++) if (str[i] != '0') {
        int delta = max(0, i - tot);
        tot += str[i] - '0' + delta;
        ret += delta;
    }
    return ret;
}

int main(){
    freopen("./A-large.in", "r", stdin);
    freopen("AAAA.out", "w", stdout);
    int ca;
    cin >> ca;
    for (int i = 0; i < ca; i++) {
        printf("Case #%d: %d\n", i + 1, solve());
    }
    return 0;
}
