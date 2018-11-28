#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
#include <cstring>
#include <vector>
#include <map>
#include <set>
using namespace std;

const int maxn = 10000 + 10;
int n, x;
int a[maxn];

int main() {    
    int T;
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &n, &x);
        for (int i = 0; i < n; i++) scanf("%d", a + i);
        sort(a, a + n);        
        int p = 0;
        int ans = 0;
        for (int i = n - 1; i >= p; i--)
            if (i == p) {
                ans++;
                break;
            } else {
                if (a[i] + a[p] <= x) {
                    ans++;
                    p++;
                } else ans++;
            }
        printf("Case #%d: %d", t, ans);
        
        printf("\n");
    }
}

