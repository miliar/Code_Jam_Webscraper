#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long ll;

char B[55];

char A[105][55];

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        int n, L;
        scanf("%d%d", &n, &L);
        for(int i = 0; i < n; ++ i) {
            scanf("%s", A[i]);
        }
        scanf("%s", B);
        printf("Case #%d: ", cas);
        bool bad = false;
        for(int i = 0; i < n; ++ i) {
            if(strcmp(B, A[i]) == 0) {
                bad = true;
                break;
            }
        }
        if(bad) {
            puts("IMPOSSIBLE");
            continue;
        }
        if(L > 1) {
            for(int i = 1; i < L; ++ i) putchar('1');
            putchar(' ');
            for(int i = 0; i < L; ++ i) printf("0?");
            puts("");
            continue;
        }
        printf("0 ?\n");
    }
    return 0;
}
