#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <cstring>
using namespace std;

int main(void) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int _case, k, c, s;
    scanf("%d", &_case);
    for (int i = 1; i <= _case; i++) {
        scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d:", i);
        for (int i = 1; i <= s; ++i)
            printf(" %d", i);
        puts("");
    }
    return 0;
}
