#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define INF 1e15

long long calculate(vector<int> &a, int t)
{
    long long additional = 0;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] > t) {
            if ((a[i] - t) % t == 0) {
                additional += (a[i] - t)/t;
            } else {
                additional += (a[i] - t)/t + 1;
            }
        } else {
            break;
        }
    }
    return additional + t;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tc;
    scanf("%d", &tc);
    for (int t = 1; t <= tc; t++) {
        printf("Case #%d: ", t);
        int n;
        scanf("%d", &n);
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }
        sort(a.rbegin(), a.rend());
        long long minimum = INF;
        for (int t = 1; t <= 1005; t++) {
            minimum = min(minimum, calculate(a, t));
        }
        printf("%lld\n", minimum);
    }
}
