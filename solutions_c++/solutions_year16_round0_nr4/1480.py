#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;

int main() {
    freopen("C:\\Users\\timur\\Downloads\\D-small-attempt0.in", "r", stdin);
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);

    for (int test = 0; test != t; ++test) {
        int k, c, s;
        scanf("%d %d %d", &k, &c, &s);
        printf("Case #%d:", test + 1);

        if (k > s) {
            printf(" IMPOSSIBLE\n");
        } else {
            for (int i = 0; i != k; ++i) {
                printf(" %d", i + 1);
            }
            printf("\n");
        }
    }

    return 0;
}