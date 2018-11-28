/*
 *
 * Tag: Implementation
 * Time: O(n)
 * Space: O(n)
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;
const int N = 10010000;
const int M = 110;
const long long MOD = 1000000007;
const double eps = 1e-10;
int c, k, s;

int main() {
    freopen("/Users/ybc/Project/CCPP/ACM/D-small-attempt0.in", "r", stdin);
    freopen("/Users/ybc/Project/CCPP/ACM/out.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    for (int cas = 1; cas <= T; ++ cas) {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d:",cas);
        if (k > s) {
            puts(" IMPOSSIBLE");
            continue;
        }
        for (int i = 1; i <= k; ++ i) {
            printf(" %d",i);
        }
        puts("");
    }
    return 0;
}