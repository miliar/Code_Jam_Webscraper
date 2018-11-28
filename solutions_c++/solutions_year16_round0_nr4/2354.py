#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <array>

using namespace std;

int k, c, s;

void solve()
{

    uint64_t maxans = k;
    for (int i = 1; i < c; i++) {
        maxans *= k;
    }
    // cerr << maxans << endl;
    uint64_t step = maxans / k;

    uint64_t i = 1;
    while (i <= maxans) {
        cout << i << " ";
        i += step;
    }
    cout << endl;
}

int main()
{
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}