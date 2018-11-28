#include <cstdio>
#include <cstdlib>

#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

const int max_n = 1e3 + 10;

int a[max_n];
int l[max_n], r[max_n];
pair<int, int> b[max_n];
int n;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    scanf("%d", &tests);
    for (int test = 1; test <= tests; ++test) {
        printf("Case #%d: ", test);
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) scanf("%d", a + i);
        for (int i = 0; i < n; ++i) {
            l[i] = r[i] = 0;
            for (int j = 0; j < i; ++j)
                if (a[j] > a[i]) ++l[i];
            for (int j = i + 1; j < n; ++j)
                if (a[j] > a[i]) ++r[i];
        }
        for (int i = 0; i < n; ++i) {
            b[i].first = a[i];
            b[i].second = i;
        }
        sort(b, b + n);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int id = b[i].second;
            ans += min(l[id], r[id]);
        }
        printf("%d\n", ans);
    }
    
    return 0;
}
