#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

const int N = 1010;
int a[N];

void run(int cas) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int c0 = 0, c1 = 0;
        for (int j = 0; j < i; j++)
            if (a[j] > a[i]) c0++;
        for (int j = i + 1; j < n; j++)
            if (a[j] > a[i]) c1++;
        ans += min(c0, c1);
    }
    printf("Case #%d: %d\n", cas, ans);
}

int main() {
    int tt, cas;
    scanf("%d", &tt);
    for (cas = 1; cas <= tt; cas++)
        run(cas);
    return 0;
}

