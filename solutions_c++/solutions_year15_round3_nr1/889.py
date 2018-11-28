#include <bits/stdc++.h>

#define maxN 1000005
#define maxC 1000000007

using namespace std;

int main() {
    #ifndef ONLINE_JUDGE
        freopen("A-large.in", "r", stdin);
        freopen("A-large.out", "w", stdout);
    #endif // ONLINE_JUDGE

    int nTest;
    scanf("%d", &nTest);
    for (int iTest = 1; iTest <= nTest; ++iTest) {
        int r, c, w;
        scanf("%d%d%d", &r, &c, &w);
        printf("Case #%d: %d\n", iTest, (r-1)*(c/w) + (c-1)/w + w);
    }
}
