#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <queue>
using namespace std;

void solve()
{
    int K, C, S;
    scanf("%d%d%d", &K, &C, &S);
    for (int i = 0; i < S; ++ i) {
        printf(" %d", i + 1);
    }
    puts("");
}

int main()
{
    int tests, test = 1;
    for (scanf("%d", &tests); test <= tests; ++ test) {
        printf("Case #%d:", test);
        solve();
    }
    return 0;
}
