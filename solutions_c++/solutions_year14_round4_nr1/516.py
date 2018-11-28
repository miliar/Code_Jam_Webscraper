#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
 
#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

typedef long long ll;

const int max_n = 1e4 + 10;

int n, x;
int a[max_n];

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    scanf("%d", &tests);
    for (int test = 1; test <= tests; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d", &n, &x);
        for (int i = 0; i < n; ++i) scanf("%d", a + i);
        int last = 0;
        sort(a, a + n);
        int ans = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (i < last) break;
            ++ans;
            int ost = x - a[i];
            if (last < i) {
                if (a[last] <= ost) {
                    ++last;
                }
            }
        }
        printf("%d\n", ans);
    }
  
  
    return 0;
}
