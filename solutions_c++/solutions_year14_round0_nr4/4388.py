#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <string.h>
using namespace std;

double naomi[1024], ken[1024];
int t, n;

int funA() {
    for (int i = 0; i < n; i++) {
        bool flag = true;
        for (int j = 0; flag && j < n - i; j++) {
            if (naomi[i + j] < ken[j])
                flag = false;
        }
        if (flag)
            return n - i;
    }
    return 0;
}

int funB() {
    int r = n - 1;
    int ret = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (naomi[i] > ken[r])
            ret++;
        else
            r--;
    }
    return ret;
}

int main() {
    freopen("td_large.in", "r", stdin);
    freopen("ans.txt", "w", stdout);
    scanf("%d", &t);
    for (int z = 1; z <= t; z++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%lf", &naomi[i]);
        for (int i = 0; i < n; i++)
            scanf("%lf", &ken[i]);
        sort(naomi, naomi + n);
        sort(ken, ken + n);

        printf("Case #%d: %d %d\n", z, funA(), funB());
    }
    return 0;
}
