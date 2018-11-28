#include <cstdio>
#include <algorithm>
#include <set>
#define MAX 10000

using namespace std;

int v[MAX];

int main() {
    int t, n;
    set<int> S;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++) {
        int k = 0;
        scanf("%d", &n);
        for (int i = 0; i < 2 * n - 1; i++)
            for (int j = 0; j < n; j++)
                scanf("%d", &v[k++]);

        sort(v, v+k);
        int i = 0;
        v[k] = 0;
        while (i < k)
            if (v[i] == v[i+1])
                i += 2;
            else
                S.insert(v[i++]);

        printf("Case #%d:", cas);
        for (set<int>::iterator it = S.begin(); it != S.end(); it++)
            printf(" %d", *it);
        printf("\n");
        S.clear();
    }
    return 0;
}
