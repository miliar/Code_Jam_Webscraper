#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <string.h>
#include <set>
#include <map>

using namespace std;

int n;
char s[5010];

bool check(int x) {
    int cur = x + s[0] - '0';
    for (int i = 1; i <= n; i++) {
        if (cur < i) {
            return false;
        }
        cur += s[i] - '0';
    }
    return true;
}

int solve() {
    cin>>n>>s;
    for (int it = 0; it <= 18*(n + 1); it++) {
        if (check(it)) {
            return it;
        }
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int test;
    cin>>test;
    for (int i = 1; i <= test; i++) {
        printf("Case #%d: %d\n", i, solve() );
    }
    return 0;
}
