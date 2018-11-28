#include <cstdio>
#include <algorithm>
#define scanf(args...) (scanf(args) ? : 0)
const int MAXN = 1e4+5;
const int MAXC = 705;

int T[MAXN];

void testCase(int t) {
    int n, x;
    scanf("%d%d", &n, &x);

    for (int i=0; i<n; i++)
        scanf("%d", &T[i]);
    std::sort(T, T+n);
    int res = 0, it1 = 0, it2 = n-1;
    while (it1 <= it2) {
        if (it1 == it2) {
            res++;
            break;
        }
        else if (T[it2]+T[it1] <= x) {
            it1++, it2--;
            res++;
        }
        else {
            res++;
            it2--;
        }

    }

    printf("Case #%d: %d\n", t, res);
}

int main() {
    int t;
    scanf("%d", &t);

    for (int test=1; test<=t; test++) {
        testCase(test);
    }
}
