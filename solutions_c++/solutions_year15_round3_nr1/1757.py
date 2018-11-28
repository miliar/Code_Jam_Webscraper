#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
using namespace std;

int solve() {
    int r, c, w;
    cin >> r >> c >> w;

    return ((((c-1) / w) + 1) * r) + (w - 1);
}

int main() {
    int t; cin >> t;
    for(int tcase = 1; tcase <= t; ++tcase)
        printf("Case #%i: %i\n", tcase, solve());
    return 0;
}
